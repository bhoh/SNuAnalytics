from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
#from keras.layers.noise import GaussianNoise
from keras.layers.normalization import BatchNormalization
from keras import initializers
from keras.optimizers import SGD, Adam

# Define initialization
def normal(shape, name=None):
  return initializers.normal(shape, scale=0.05, name=name)

# Generate model
class KerasModel():

  def __init__(self):
    self.model = Sequential()


  def defineModel_3layer(self,input_dim_):
    # Define model
    
    #
    # we can think of this chunk as the input layer
    self.model.add(Dense(200, input_dim=input_dim_, kernel_initializer=initializers.he_normal(seed=1231)))
    self.model.add(BatchNormalization())
    ## noise
    #self.model.add(GaussianNoise(1.))
    self.model.add(Activation('relu'))
    self.model.add(Dropout(0.4))

    # we can think of this chunk as the input layer
    self.model.add(Dense(100, kernel_initializer=initializers.he_normal(seed=1232)))
    self.model.add(BatchNormalization())
    ## noise
    #self.model.add(GaussianNoise(1.))
    self.model.add(Activation('relu'))
    self.model.add(Dropout(0.4))

    # we can think of this chunk as the hidden layer    
    self.model.add(Dense(75, kernel_initializer=initializers.he_normal(seed=1233)))
    self.model.add(BatchNormalization())
    ## noise
    #self.model.add(GaussianNoise(1.))
    self.model.add(Activation('relu'))
    self.model.add(Dropout(0.4))

    # we can think of this chunk as the output layer
    self.model.add(Dense(2, kernel_initializer=initializers.RandomUniform(minval=-0.05, maxval=0.05, seed=1234)))
    self.model.add(BatchNormalization())
    self.model.add(Activation('softmax'))

    #self.model.add(Dense(64, kernel_initializer=initializers.he_normal(seed=None), activation='relu', input_dim=input_dim_))
    #self.model.add(Dense(32, kernel_initializer=initializers.he_normal(seed=None), activation='relu'))
    #self.model.add(Dense(2, kernel_initializer=initializers.he_normal(seed=None), activation='softmax'))

  def compile(self,loss_='categorical_crossentropy',
		   #optimizer_=SGD(lr=0.1,decay=1e-5),
		   optimizer_=Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False),
		   metrics_=['accuracy',]
	     ):
    # Set loss and optimizer
    self.model.compile(loss=loss_, optimizer=optimizer_, metrics=metrics_)

  def save(self, modelName="model.h5"):
    self.model.save(modelName)
  
  def summary(self):
    self.model.summary()

	       
		  
