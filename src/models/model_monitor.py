import yaml
import argparse
import pandas as pd
import numpy as np

from evidently.report import Report
# from evidently.dashboard import Dashboard
# from evidently.dashboard.tabs import DataDriftTab,CatTargetDriftTab
from evidently.metric_preset import DataDriftPreset,TargetDriftPreset,DataQualityPreset

def read_params(config_path):
    """
    read parameters from the params.yaml file
    input: params.yaml location
    output: parameters as dictionary
    """
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def model_monitoring(config_path):
    config = read_params(config_path)
    train_data_path = config["raw_data_config"]["raw_data_csv"]
    new_train_data_path=config["raw_data_config"]["new_train_data_csv"]
    target = config["raw_data_config"]["target"]
    monitor_dashboard_path = config["model_monitor"]["monitor_dashboard_html"]
    monitor_dashboard_path_json= config["model_monitor"]["monitor_dashboard_json"]
    monitor_target = config["model_monitor"]["target_col_name"]

    ref=pd.read_csv(train_data_path)
    cur=pd.read_csv(new_train_data_path)

    ref=ref.rename(columns ={target:monitor_target}, inplace = False)
    cur=cur.rename(columns ={target:monitor_target}, inplace = False)

    report = Report(metrics=[DataDriftPreset(),TargetDriftPreset()])
    # report.run(reference_data=reference, current_data=current)

    # data_and_target_drift_dashboard = Dashboard(tabs=[DataDriftTab(),CatTargetDriftTab()])
    report.run(reference_data=ref, current_data=cur)
    report.save_html(monitor_dashboard_path)
    report.save_json(monitor_dashboard_path_json)

    dp = pd.read_json(monitor_dashboard_path_json)
    drift_score=[]
    for column in ref.columns:
        drift_score.append(dp['metrics'][1]['result']['drift_by_columns'][column]['drift_score'])
    drift = np.mean(drift_score)
    print("Drift Score:",drift)

    config["model_monitor"]["drift_score"]= float(drift)
    with open(config_path, "w") as f:
        yaml.dump(config, f)


if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    model_monitoring(config_path=parsed_args.config)