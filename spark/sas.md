# SAS datasets

## Just put the sas datasets in hdfs and read them using spark/pyspark 
the best thing about this approach is that sas datatypes map nicely to spark datatypes and you don't have to manually cast anything - 

# Pyspark
```
os.environ["PYSPARK_SUBMIT_ARGS"] = ("--driver-memory 2g --jars /data/custom-jars/sas/log4j-api-scala_2.11-2.7.jar,/data/custom-jars/sas/slf4j-api-1.7.5.jar,/data/custom-jars/sas/parso-2.0.8.jar,/data/custom-jars/sas/scala-reflect-2.11.8.jar,/data/custom-jars/sas/spark-sas7bdat_2.11-2.0.0.jar pyspark-shell")
spark = SparkSession.builder.appName("PythonLR").getOrCreate()
sc = spark.sparkContext
df = spark.read.format("com.github.saurfang.sas.spark").load("/sas/sg/data/onshore/deposit/dataset/casatxn1_201805.sas7bdat")
#Show sample records from the dataset
df.show(10)
```

# Scala
```
%AddJar file:///data/custom-jars/sas/spark-sas7bdat_2.11-2.0.0.jar
%AddJar file:///data/custom-jars/sas/parso-2.0.8.jar
import org.apache.spark.sql.SQLContext
import com.github.saurfang.sas.spark._
val df = spark.read.format("com.github.saurfang.sas.spark").load("/sas/sg/data/onshore/deposit/dataset/casatxn1_201805.sas7bdat")
df.show(10)
```

## regular local R/Python and read sasd atasets from local filesystem using -
# Python
```
import pandas as pd
from sas7bdat import SAS7BDAT
with SAS7BDAT('/home/cdsw/sas/casatxn1_201805.sas7bdat') as file:
  df_sas = file.to_data_frame()
df_sas
```

# R
```
install.packages("sas7bdat")
library("sas7bdat")
df = read.sas7bdat("/home/cdsw/sas/casatxn1_201805.sas7bdat")
df
```
