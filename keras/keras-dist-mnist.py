## https://wiki.cloudera.com/display/~christopher.royles/Deep+Learning+Shortest+Paths
# WARNING
# Keras-dist requires that all native libraries are installed on all nodes.  This version works to a point, but I was unable to find a suitable way to distribute the native framework.
# Results in Tensorflow level errors that native tensorflow libraries are not available.

# CDSW python3 2cpu 4GB
# !pip install --upgrade dist-keras
 
# !mkdir data
# !cd data
# !wget https://github.com/cerndb/dist-keras/raw/master/examples/data/mnist.zip
# !unzip mnist.zip
# !hadoop fs -copyFromLocal ~/data/ .
 
# !git clone https://github.com/keras-team/keras.git
# !cd dist-keras
# !zip -r keras.zip keras
 
# !git clone https://github.com/cerndb/dist-keras.git
# !cd dist-keras
# !zip -r distkeras.zip distkeras
 
import cdsw
from pyspark.sql import SparkSession
 
import numpy as np
import seaborn as sns
 
from keras.optimizers import *
from keras.models import Sequential
from keras.layers.core import *
from keras.layers.convolutional import *
 
 
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
 
from pyspark.ml.feature import StandardScaler
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import OneHotEncoder
from pyspark.ml.feature import MinMaxScaler
from pyspark.ml.feature import StringIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
 
from distkeras.trainers import *
from distkeras.predictors import *
from distkeras.transformers import *
from distkeras.evaluators import *
from distkeras.utils import *
 
path_train = "data/mnist_train.csv"
path_test = "data/mnist_test.csv"
 
spark = SparkSession.builder \
      .appName("helloworld-dist-keras") \
      .getOrCreate()
   
sc=spark.sparkContext   
sc.addPyFile("/home/cdsw/dist-keras/distkeras.zip")
sc.addPyFile("/home/cdsw/keras/keras.zip")   
sc.addPyFile("/home/cdsw/tensorflow.zip")    
     
reader = spark
 
raw_dataset_train = reader.read.format('csv') \
                          .options(header='true', inferSchema='true') \
                          .load(path_train)
# Read the testing dataset.
raw_dataset_test = reader.read.format('csv') \
                         .options(header='true', inferSchema='true') \
                         .load(path_test)
     
     
     
# First, we would like to extract the desired features from the raw dataset.
# We do this by constructing a list with all desired columns.
# This is identical for the test set.
features = raw_dataset_train.columns
features.remove('label')
 
# Next, we use Spark's VectorAssembler to "assemble" (create) a vector of all desired features.
# http://spark.apache.org/docs/latest/ml-features.html#vectorassembler
vector_assembler = VectorAssembler(inputCols=features, outputCol="features")
# This transformer will take all columns specified in features, and create an additional column "features" which will contain all the desired features aggregated into a single vector.
dataset_train = vector_assembler.transform(raw_dataset_train)
dataset_test = vector_assembler.transform(raw_dataset_test)
 
 
# Define the number of output classes.
nb_classes = 10
encoder = OneHotTransformer(nb_classes, input_col="label", output_col="label_encoded")
dataset_train = encoder.transform(dataset_train)
dataset_test = encoder.transform(dataset_test)
 
def show_instances(column):
    global dataset
 
    num_instances = 6 # Number of instances you would like to draw.
    x_dimension   = 3 # Number of images to draw on the x-axis.
    y_dimension   = 2 # Number of images to draw on the y-axis.
 
    # Fetch 3 different instance from the dataset.
    instances = dataset_train.select(column).take(num_instances)
    # Process the instances.
    for i in range(0, num_instances):
        instance = instances[i]
        instance = instance[column].toArray().reshape((28, 28))
        instances[i] = instance
 
    # Draw the sampled instances.
    fig, axn = plt.subplots(y_dimension, x_dimension, sharex=True, sharey=True)
    num_axn = len(axn.flat)
    for i in range(0, num_axn):
        ax = axn.flat[i]
        h = sns.heatmap(instances[i], ax=ax)
        h.set_yticks([])
        h.set_xticks([])
         
         
show_instances("features")
 
# Clear the dataset in the case you ran this cell before.
dataset_train = dataset_train.select("features", "label", "label_encoded")
dataset_test = dataset_test.select("features", "label", "label_encoded")
# Allocate a MinMaxTransformer using Distributed Keras.
# o_min -> original_minimum
# n_min -> new_minimum
transformer = MinMaxTransformer(n_min=0.0, n_max=1.0, \
                                o_min=0.0, o_max=250.0, \
                                input_col="features", \
                                output_col="features_normalized")
# Transform the dataset.
dataset_train = transformer.transform(dataset_train)
dataset_test = transformer.transform(dataset_test)
 
 
show_instances("features_normalized")
 
reshape_transformer = ReshapeTransformer("features_normalized", "matrix", (28, 28, 1))
dataset_train = reshape_transformer.transform(dataset_train)
dataset_test = reshape_transformer.transform(dataset_test)
 
mlp = Sequential()
mlp.add(Dense(1000, input_shape=(784,)))
mlp.add(Activation('relu'))
mlp.add(Dense(250))
mlp.add(Activation('relu'))
mlp.add(Dense(10))
mlp.add(Activation('softmax'))
 
mlp.summary()
 
optimizer_mlp = 'adam'
loss_mlp = 'categorical_crossentropy'
 
# Taken from Keras MNIST example.
 
# Declare model parameters.
img_rows, img_cols = 28, 28
# number of convolutional filters to use
nb_filters = 32
# size of pooling area for max pooling
pool_size = (2, 2)
# convolution kernel size
kernel_size = (3, 3)
input_shape = (img_rows, img_cols, 1)
 
# Construct the model.
convnet = Sequential()
convnet.add(Convolution2D(nb_filters, kernel_size[0], kernel_size[1],
                          border_mode='valid',
                          input_shape=input_shape))
convnet.add(Activation('relu'))
convnet.add(Convolution2D(nb_filters, kernel_size[0], kernel_size[1]))
convnet.add(Activation('relu'))
convnet.add(MaxPooling2D(pool_size=pool_size))
 
convnet.add(Flatten())
convnet.add(Dense(225))
convnet.add(Activation('relu'))
convnet.add(Dense(nb_classes))
convnet.add(Activation('softmax'))
 
convnet.summary()
 
optimizer_convnet = 'adam'
loss_convnet = 'categorical_crossentropy'
 
def evaluate_accuracy(model, test_set, features="features_normalized_dense"):
    evaluator = AccuracyEvaluator(prediction_col="prediction_index", label_col="label")
    predictor = ModelPredictor(keras_model=model, features_col=features)
    transformer = LabelIndexTransformer(output_dim=nb_classes)
    test_set = test_set.select(features, "label")
    test_set = predictor.predict(test_set)
    test_set = transformer.transform(test_set)
    score = evaluator.evaluate(test_set)
     
    return score
 
 
dataset_train.printSchema()
 
dataset_train = dataset_train.select("features_normalized", "matrix","label", "label_encoded")
dataset_test = dataset_test.select("features_normalized", "matrix","label", "label_encoded")
 
dense_transformer = DenseTransformer(input_col="features_normalized", output_col="features_normalized_dense")
dataset_train = dense_transformer.transform(dataset_train)
dataset_test = dense_transformer.transform(dataset_test)
dataset_train.repartition(num_workers)
dataset_test.repartition(num_workers)
 
# Assing the training and test set.
training_set = dataset_train.repartition(num_workers)
test_set = dataset_test.repartition(num_workers)
# Cache them.
training_set.cache()
test_set.cache()
 
print(training_set.count())
 
trainer = DOWNPOUR(keras_model=mlp, worker_optimizer=optimizer_mlp, loss=loss_mlp, num_workers=num_workers,
                   batch_size=4, communication_window=5, num_epoch=1,
                   features_col="features_normalized_dense", label_col="label_encoded")
trained_model = trainer.train(training_set)
 
print("Training time: " + str(trainer.get_training_time()))
print("Accuracy: " + str(evaluate_accuracy(trained_model, test_set)))
 
trainer.parameter_server.num_updates
 
trainer = ADAG(keras_model=mlp, worker_optimizer=optimizer_mlp, loss=loss_mlp, num_workers=num_workers,
               batch_size=4, communication_window=15, num_epoch=1,
               features_col="features_normalized_dense", label_col="label_encoded")
trained_model = trainer.train(training_set)
 
print("Training time: " + str(trainer.get_training_time()))
print("Accuracy: " + str(evaluate_accuracy(trained_model, test_set)))
 
trainer.parameter_server.num_updates
