from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.layers import Input, Add, Lambda, Conv1D, GRU, MaxPooling1D, Flatten, Reshape, TimeDistributed, Concatenate
#from keras.layers.noise import GaussianNoise
from keras.layers.normalization import BatchNormalization
from keras import initializers
from keras import regularizers
from keras.optimizers import SGD, Adam, Nadam, RMSprop
from keras.models import Model 

from keras import backend as K

import numpy as np

# Define initialization
def normal(shape, name=None):
  return initializers.normal(shape, scale=0.05, name=name)

# Generate model
class KerasModel():

  def __init__(self):
    #self.model = Sequential()
    # limit 10 core
    #K.set_session(K.tf.Session(config=K.tf.ConfigProto(intra_op_parallelism_threads=10, inter_op_parallelism_threads=10)))

    self.model = None


  def defineModel_3layer(self,input_dim_):
    # Define model

    def conv1Dres(X,num_filter):
      res = Conv1D(num_filter,3,activation='relu',padding='same',kernel_regularizer=regularizers.l1_l2(l1=1e-7, l2=0))(X)
      res = Conv1D(num_filter,3,padding='same',kernel_regularizer=regularizers.l1_l2(l1=1e-7, l2=0))(res)
      out = Add()([X,res])
      out = Activation('relu')(out)
      return Dropout(0.20)(out)
    
    inputs = Input(shape=(input_dim_,))
    X = Reshape((input_dim_,1))(inputs)
    X = conv1Dres(X,32)
    X = conv1Dres(X,32)
    X = MaxPooling1D(2,padding='same')(X)
    X = conv1Dres(X,32)
    X = conv1Dres(X,32)
    X = MaxPooling1D(2,padding='same')(X)
    # each filters are considered as a time stamp
    X = GRU(32,dropout=0.20,recurrent_dropout=0.20,return_sequences=True, kernel_regularizer=regularizers.l1_l2(l1=0, l2=1e-4),recurrent_regularizer=regularizers.l1_l2(l1=0, l2=1e-4))(X)
    X = GRU(16,dropout=0.20,recurrent_dropout=0.20,return_sequences=True, kernel_regularizer=regularizers.l1_l2(l1=0, l2=1e-4),recurrent_regularizer=regularizers.l1_l2(l1=0, l2=1e-4))(X)

    # disable the following when using time distributed  
    #self.model.add(Flatten()) # num layer = (num filter) * (num input node)

    # we can think of this chunk as the input layer
    # not using time distributed.
    # time distributed layer make a layer by each time stamp
    #X = TimeDistributed(Dense(1, kernel_initializer=initializers.he_normal(seed=1232), kernel_regularizer=regularizers.l1_l2(l1=0, l2=1e-4)))(X)
    #self.model.add(Dense(64, kernel_initializer=initializers.he_normal(seed=1232), kernel_regularizer=regularizers.l1_l2(l1=1e-4, l2=1e-4)))
    #X = BatchNormalization()(X)
    #X = Activation('relu')(X)

    # enable this when using time distributed  
    X = Flatten()(X)

    #X = Dense(100, kernel_initializer=initializers.he_normal(seed=1232), kernel_regularizer=regularizers.l1_l2(l1=0, l2=1e-4))(X)
    #X = BatchNormalization()(X)
    #X = Activation('relu')(X)
    #X = Dropout(0.5)(X)

    # we can think of this chunk as the output layer
    X = Dense(2, kernel_initializer=initializers.RandomUniform(minval=-0.05, maxval=0.05, seed=1234), kernel_regularizer=regularizers.l1_l2(l1=0, l2=1e-4))(X)
    X = Activation('softmax')(X)
    self.model = Model(inputs, X)

    #self.model.add(Dense(64, kernel_initializer=initializers.he_normal(seed=None), activation='relu', input_dim=input_dim_))
    #self.model.add(Dense(32, kernel_initializer=initializers.he_normal(seed=None), activation='relu'))
    #self.model.add(Dense(2, kernel_initializer=initializers.he_normal(seed=None), activation='softmax'))

  def compile(self,lossftn='categorical_crossentropy',
		   #optimizer_=SGD(lr=0.1,decay=1e-5),
           # default lr=0.001
		   #optimizer_=Adam(lr=0.1, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.1),
		   optimizer_=Nadam(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=None, schedule_decay=0.004),
           #optimizer_=RMSprop(lr=0.001, rho=0.9, epsilon=None, decay=0.0),
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
	       
		  