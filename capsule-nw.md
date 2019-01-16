# Capsule Network

Capsule Networks: A new and attractive AI architecture
https://heartbeat.fritz.ai/capsule-networks-a-new-and-attractive-ai-architecture-bd1198cc8ad4

activation function: squash function
normalize the magnitude of vectors, rather than the scalar elements themselves

Capsule Layer

```python
def CapsNet(input_shape, n_class, num_routing):
    """
    MNIST Dataset for Capsule Networks.
       : "input_shape" parameter: vdata shape, 3d, [w,h,c]
       : "n_class" parameter: number of classes
       : "num_routing" parameter: dynamic routing number of iteration
       : Function output: two Keras model, first for training, second for evalaution.
            `eval_model` used for traning at the same time.
    """
    x = layers.Input(shape=input_shape )

    # LAYER 1: Convolution Layer (Conv2D)
    conv1 = layers.Conv2D(filters=256, kernel_size=9, strides=1, padding='valid', activation='relu', name='conv1')(x)

    # LAYER 2: Conv2D squash activation, [None, num_capsule, dim_capsule] fro reshaping.
    primarycaps = PrimaryCap(conv1, dim_capsule=8, n_channels=32, kernel_size=9, strides=2, padding='valid')

    # LAYER 3: Capsule Layers. Run: Dynamic routing algorithm.
    digitcaps = CapsuleLayer(num_capsule=n_class, dim_capsule=16, num_routing=num_routing,
                             name='digitcaps')(primarycaps)

    # LAYER 4:
    # If you use Tensorflow you can skip this session :)

    out_caps = Length(name='capsnet')(digitcaps)
 ```
 
 ```python
 class CapsuleLayer(layers.Layer):
    """
    The capsule layer. It is similar to Dense layer. Dense layer has `in_num` inputs, each is a scalar, the output of the 
    neuron from the former layer, and it has `out_num` output neurons. CapsuleLayer just expand the output of the neuron
    from scalar to vector. So its input shape = [None, input_num_capsule, input_dim_capsule] and output shape = \
    [None, num_capsule, dim_capsule]. For Dense Layer, input_dim_capsule = dim_capsule = 1.
    
    :param num_capsule: number of capsules in this layer
    :param dim_capsule: dimension of the output vectors of the capsules in this layer
    :param routings: number of iterations for the routing algorithm
    """
    def __init__(self, num_capsule, dim_capsule, routings=3,
                 kernel_initializer='glorot_uniform',
                 **kwargs):
        super(CapsuleLayer, self).__init__(**kwargs)
        self.num_capsule = num_capsule
        self.dim_capsule = dim_capsule
        self.routings = routings
        self.kernel_initializer = initializers.get(kernel_initializer)

    def build(self, input_shape):
        assert len(input_shape) >= 3, "The input Tensor should have shape=[None, input_num_capsule, input_dim_capsule]"
        self.input_num_capsule = input_shape[1]
        self.input_dim_capsule = input_shape[2]

        # Transform matrix
        self.W = self.add_weight(shape=[self.num_capsule, self.input_num_capsule,
                                        self.dim_capsule, self.input_dim_capsule],
                                 initializer=self.kernel_initializer,
                                 name='W')

 ```
