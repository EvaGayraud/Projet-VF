from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


def create_mlp(dim, regress=False):

	# define the MLP network
	model = Sequential()
	model.add(Dense(8, input_dim=dim, activation="relu"))
	model.add(Dense(4, activation="relu"))

	if regress:
		model.add(Dense(1, activation="linear"))

	return model

