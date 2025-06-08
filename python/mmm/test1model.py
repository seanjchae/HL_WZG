import torch
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):

    def __init__(self):
        super(Model, self).__init__()
        self.flatten = nn.Flatten()

        # Increased neuron count for deeper layers
        self.fc = nn.Sequential(

            # 1st layer: 1024 neurons
            nn.Linear(10, 1024),
            nn.ReLU(),
            nn.BatchNorm1d(1024),
            nn.Dropout(0.5),

            # 2nd layer: 512 neurons
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.BatchNorm1d(512),
            nn.Dropout(0.5),

            # 3rd layer: 256 neurons
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.BatchNorm1d(256),
            nn.Dropout(0.5),

            # 4th layer: 128 neurons
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.BatchNorm1d(128),
            nn.Dropout(0.5),

            # 5th layer: 64 neurons
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.BatchNorm1d(64),

            # Output layer: 1 neuron with sigmoid for binary classification
            nn.Linear(64, 1),
            nn.Sigmoid(),
        )

    def forward(self, x):
        y_pred = self.fc(x)
        return y_pred

# Example instantiation
if __name__ == "__main__":
    model = Model()
    example_input = torch.randn(1, 10)  # Example input with 10 features
    output = model(example_input)
    print(f"Model output: {output}")
