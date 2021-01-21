import tensorflow as tf
import numpy as np
import tensorflow.keras as keras
import argparse

X = np.arange(1,10)
Y = np.arange(1,10)*2 +5

parser = argparse.ArgumentParser()
parser.add_argument('--epochs', type = int , default=2)
args, _ = parser.parse_known_args()

model = keras.models.Sequential([
    
    keras.layers.Dense(1)
    
])

model.compile(loss = 'mse', optimizer='sgd')
history = model.fit(X,Y, epochs = args.epochs)