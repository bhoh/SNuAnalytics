from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.regularizers import l2
from keras.layers.normalization import BatchNormalization
from keras import initializers
from keras.optimizers import SGD
from keras.utils import plot_model

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

  def setHiddenLayers(self, n_Nodes_Input, n_Nodes_Hidden, n_hidden_Layers, activ='relu', l2_val = 1e-5):
    #self.model.add( Dense( n_Nodes_Hidden, activation=activ, W_regularizer=l2(l2_val), input_dim = n_Nodes_Input) )
    self.model.add( Dense( n_Nodes_Hidden, activation=activ, input_dim = n_Nodes_Input) )
    for k in range(n_hidden_Layers - 1):
      #self.model.add( Dense( n_Nodes_Hidden, activation=activ, W_regularizer=l2(l2_val))  )
      self.model.add( Dense( n_Nodes_Hidden, activation=activ)  )

  def setOutLayer(self, n_Nodes_Out, activ = 'softmax'):
    # Output layer
    # NOTE: Use following output types for the different tasks
    # Binary classification: 2 output nodes with 'softmax' activation
    # Regression: 1 output with any activation ('linear' recommended)
    # Multiclass classification: (number of classes) output nodes with 'softmax' activation
    self.model.add(Dense(n_Nodes_Out, activation=activ))

  def compile(self,lossftn='categorical_crossentropy',
		   SGD_lr=0.1, SGD_decay=1e-5,
		   metrix=['accuracy',]
	     ):
    # Set loss and optimizer
    self.model.compile(loss=lossftn, optimizer=SGD(SGD_lr, SGD_decay), metrics=metrix)

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
	       
		  
