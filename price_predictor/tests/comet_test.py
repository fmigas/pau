
from src.config import comet_config
from comet_ml import Experiment

# Create an experiment with your API key
experiment = Experiment(
    api_key = comet_config.comet_api_key,
    project_name = comet_config.comet_project_name,
    workspace = "fmigas",
)

# Log parameters
params = {
    "learning_rate": 0.001,
    "batch_size": 32,
    "num_epochs": 10
}
experiment.log_parameters(params)

# Log metrics
for epoch in range(1, params["num_epochs"] + 1):
    # Simulate some metrics
    accuracy = 0.8 + epoch * 0.01
    loss = 0.5 - epoch * 0.01

    experiment.log_metric("accuracy", accuracy, step = epoch)
    experiment.log_metric("loss", loss, step = epoch)

# Log other information
experiment.log_text("This is a sample log message.")
experiment.log_other("note", "This is a note about the experiment.")

# End the experiment
experiment.end()
