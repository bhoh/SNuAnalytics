import tensorflow as tf
gpus = tf.config.list_physical_devices('GPU')
print(gpus)

from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())


from keras import backend as K
s = K.tensorflow_backend._get_available_gpus()
print(s)


