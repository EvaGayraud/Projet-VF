"""apply random forest algorithm or XGBoost"""
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
import numpy as np
import argparse
import locale
import os
import loadingfile
import models
from sklearn.metrics import r2_score

# construct the argument parser and parse the arguments

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", type=str, required=True,
	help="give house attributes to predict the value of a property")
args = vars(ap.parse_args())

print("Loading house attributes...")
inputPath = 'adress GIT'
df = loadingfile.load_house_attributes(inputPath)

print("Constructing training/testing split...")
(train, test) = train_test_split(df, test_size=0.25, random_state=42)

maxPrice = train["Valeur fonciere"].max()
trainY = train["Valeur fonciere"] / maxPrice
testY = test["Valeur fonciere"] / maxPrice

print("Processing data...")
(trainX, testX) = loadingfile.process_house_attributes(df, train, test)

model = models.create_mlp(trainX.shape[1], regress=True)
opt = Adam(lr=1e-3, decay=1e-3 / 200)
model.compile(loss="mean_absolute_percentage_error", optimizer=opt)

print("Training model...")
model.fit(x=trainX, y=trainY, validation_data=(testX, testY), epochs=200, batch_size=8)

predY = model.predict(testX)
print("The Score with ", (r2_score(predY, testY)))

