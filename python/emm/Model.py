import torch
import torch.nn as nn
import torch.nn.functional as F

neurons = 2048

class Model(nn.Module):

	def __init__(self):
		super(Model, self).__init__()
		self.flatten = nn.Flatten()
		self.fc = nn.Sequential(

			# 1st layer
			nn.Linear(23, neurons),
			nn.ReLU(),
			nn.BatchNorm1d(neurons),
			nn.Dropout(0.5),
			
			# 2nd layer
            		nn.Linear(neurons, neurons),
			nn.ReLU(),
			nn.BatchNorm1d(neurons),
			nn.Dropout(0.5),
			
			# 3rd layer
	       		nn.Linear(neurons, neurons),
			nn.ReLU(),
			nn.BatchNorm1d(neurons),
			nn.Dropout(0.5),

             		# 4th layer
			nn.Linear(neurons, neurons),
			nn.ReLU(),
			nn.BatchNorm1d(neurons),
			nn.Dropout(0.5),

            		# 5th layer
#	       		nn.Linear(neurons, neurons),
#			nn.ReLU(),
#			nn.BatchNorm1d(neurons),
#			nn.Dropout(0.5),

			# 7th layer
			nn.Linear(neurons, 64),
			nn.ReLU(),
			nn.BatchNorm1d(64),

			# 8th layer
            		nn.Linear(64, 1),
			nn.Sigmoid(),
		)


	def forward(self, x):
		y_pred = self.fc(x)
		return y_pred
