# run this in desktop
# this require administrative permission

import keras
f = keras.models.load_model("TrainedModel_DNN.h5")
from keras.utils.vis_utils import plot_model
plot_model(f, to_file='model_plot.png', show_shapes=True, show_layer_names=True)
