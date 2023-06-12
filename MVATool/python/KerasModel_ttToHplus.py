from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.layers import Add, Lambda
from keras.constraints import unit_norm
#from keras.layers.noise import GaussianNoise
from keras.layers.normalization import BatchNormalization
from keras import initializers
from keras import regularizers
from keras.optimizers import SGD, Adam, Nadam, Adadelta

import numpy as np

# Define initialization
def normal(shape, name=None):
  return initializers.normal(shape, scale=0.05, name=name)

# Generate model
class KerasModel():

  def __init__(self, index1=0,index2=0):
    self.model = Sequential()
    self.grid_search(index1, index2)


  def grid_search(self,index1,index2):
    node = [[400,200,100], [256,128,64], [200,100,50]]
    l2_norm = [1e-4, 5e-3, 1e-3]

    self.node    = node[index1]
    self.l2_norm = l2_norm[index2]


  def defineModel_3layer(self,input_dim_):
    # Define model
    
    #
    # we can think of this chunk as the input layer
    self.model.add(Lambda(lambda X : X, input_shape=(input_dim_,))) #dummy Lamda layer for test
    self.model.add(BatchNormalization())

    self.model.add(Dense(self.node[0], kernel_initializer=initializers.he_normal(seed=1231), kernel_regularizer=regularizers.l1_l2(l1=0., l2=self.l2_norm)))
    #self.model.add(Dense(256, kernel_initializer=initializers.he_normal(seed=1231), kernel_constraint=unit_norm()))
    self.model.add(BatchNormalization())
    self.model.add(Activation('elu'))
    self.model.add(Dropout(0.50))

    # we can think of this chunk as the input layer
    self.model.add(Dense(self.node[1], kernel_initializer=initializers.he_normal(seed=1232), kernel_regularizer=regularizers.l1_l2(l1=0., l2=self.l2_norm)))
    #self.model.add(Dense(128, kernel_initializer=initializers.he_normal(seed=1232), kernel_constraint=unit_norm()))
    self.model.add(BatchNormalization())
    self.model.add(Activation('elu'))
    self.model.add(Dropout(0.50))

    # we can think of this chunk as the input layer
    self.model.add(Dense(self.node[2], kernel_initializer=initializers.he_normal(seed=1232), kernel_regularizer=regularizers.l1_l2(l1=0., l2=self.l2_norm)))
    #self.model.add(Dense(64, kernel_initializer=initializers.he_normal(seed=1232), kernel_constraint=unit_norm()))
    self.model.add(BatchNormalization())
    self.model.add(Activation('elu'))
    self.model.add(Dropout(0.50))


    # we can think of this chunk as the output layer
    self.model.add(Dense(2, kernel_initializer=initializers.RandomUniform(minval=-0.05, maxval=0.05, seed=1234)))
    self.model.add(Activation('softmax'))

    #self.model.add(Dense(64, kernel_initializer=initializers.he_normal(seed=None), activation='relu', input_dim=input_dim_))
    #self.model.add(Dense(32, kernel_initializer=initializers.he_normal(seed=None), activation='relu'))
    #self.model.add(Dense(2, kernel_initializer=initializers.he_normal(seed=None), activation='softmax'))

  def compile(self,lossftn='categorical_crossentropy',
		   #optimizer_=SGD(lr=0.1,decay=1e-5),
           # default lr=0.001
		   #optimizer_=Adam(lr=0.1, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.1),
		   #optimizer_=Nadam(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=None, schedule_decay=0.004),
		   optimizer_=Adadelta(lr=1.0, rho=0.95, epsilon=None, decay=0.0, clipnorm=0.1),
		   metrics_=['accuracy',]
	     ):
    # Set loss and optimizer
    self.model.compile(loss=lossftn, optimizer=optimizer_, metrics=metrics_)

  def save(self, modelName="model.h5"):
    self.model.save(modelName)
  
  def summary(self):
    self.model.summary()

  def plot_mymodel(self,outFile='model.png'):
    print 'plot model............'
    try:
      plot_model(self.model,  to_file=outFile, show_shapes = False)
    except:
      print('[INFO] Failed to make model plot')
	       
		  
