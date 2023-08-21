import json
import yaml
import joblib
import argparse
import optuna
import sklearn
import mlflow
from optuna.integration.mlflow import MLflowCallback
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score, roc_auc_score, classification_report
from sklearn.ensemble import RandomForestClassifier


mlflow.set_tracking_uri("http://172.27.35.66:8000")
mlflow.set_experiment("Churn_mlops")

def read_params(config_path):
    """
    read parameters from the params.yaml file
    input: params.yaml location
    output: parameters as dictionary
    """
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_feat_and_target(df,target):
    """
    Get features and target variables seperately from given dataframe and target
    input: dataframe and target column
    output: two dataframes for x and y
    """
    x=df.drop(target,axis=1)
    y=df[[target]]
    return x,y
def optimize(config_path):
    config = read_params(config_path)
    train_data_path = config["processed_data_config"]["train_data_csv"]
    test_data_path = config["processed_data_config"]["test_data_csv"]
    target = config["raw_data_config"]["target"]
    max_depth=config["random_forest"]["max_depth"]
    n_estimators=config["random_forest"]["n_estimators"]

    train = pd.read_csv(train_data_path, sep=",")
    test = pd.read_csv(test_data_path, sep=",")
    train_x,train_y=get_feat_and_target(train,target)
    test_x,test_y=get_feat_and_target(test,target)

    mlflc = MLflowCallback(
        tracking_uri="http://172.27.35.85:5000",
        metric_name="AUC",create_experiment=False
    )
    import pickle
    @mlflc.track_in_mlflow()
    def objective(trial):
        n_estimators = trial.suggest_int('n_estimators', 2, 12)
        max_depth = int(trial.suggest_int('max_depth', 1, 32))
        clf = sklearn.ensemble.RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)
        mlflow.log_param("Optuna_trial_num", trial.number)
        return sklearn.model_selection.cross_val_score(clf, train_x, train_y,n_jobs=-1, cv=3).mean()

    study = optuna.create_study(study_name="ChurnPredcition_Optimization",
                                direction="maximize")
    study.optimize(objective, n_trials=5, callbacks=[mlflc])

    # Getting the best trial:
    print(f"The best trial is : \n{study.best_trial}")

    # Getting the best score:
    print(f"The best value is : \n{study.best_value}")

    # Getting the best parameters:
    print(f"The best parameters are : \n{study.best_params}")
    print("max_depth",study.best_params['max_depth'])
    print("n_estimators",study.best_params['n_estimators'])

    config["random_forest"]["max_depth"]=study.best_params['max_depth']
    config["random_forest"]["n_estimators"]=study.best_params['n_estimators']
    with open(config_path, "w") as f:
        yaml.dump(config, f)

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    optimize(config_path=parsed_args.config)


