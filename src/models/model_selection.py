import joblib
import mlflow
import argparse
from pprint import pprint
from train_model import read_params
from mlflow.tracking import MlflowClient

def log_production_model(config_path):
    config = read_params(config_path)
    mlflow_config = config["mlflow_config"]
    model_name = mlflow_config["registered_model_name"]
    model_dir = config["model_dir"]
    remote_server_uri = mlflow_config["remote_server_uri"]

    mlflow.set_tracking_uri(remote_server_uri)
    # Load all runs from experiment
    experiment_id = mlflow.get_experiment_by_name("Churn").experiment_id
    all_runs = mlflow.search_runs(experiment_ids=experiment_id, order_by=["metrics.accuracy DESC"])
    # Best run
    best_run_id = all_runs.iloc[0].run_id
    # best_run = mlflow.get_run(run_id=best_run_id)
    # runs = mlflow.search_runs(experiment_ids=1)
    # max_accuracy = max(runs["metrics.accuracy"])
    # max_accuracy_run_id = list(runs[runs["metrics.accuracy"] == max_accuracy]["run_id"])[0]

    client = MlflowClient()
    for mv in client.search_model_versions(f"name='{model_name}'"):
        mv = dict(mv)
        if mv["run_id"] == best_run_id:
            current_version = mv["version"]
            logged_model = mv["source"]
            pprint(mv, indent=4)
            client.transition_model_version_stage(
                name=model_name,
                version=current_version,
                stage="Production"
            )
        else:
            current_version = mv["version"]
            client.transition_model_version_stage(
                name=model_name,
                version=current_version,
                stage="Staging"
            )
            logged_model = f'runs:/{best_run_id}/{mlflow_config["registered_model_name"]}'
    
    loaded_model = mlflow.pyfunc.load_model(logged_model)
    joblib.dump(loaded_model, model_dir)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data = log_production_model(config_path=parsed_args.config)