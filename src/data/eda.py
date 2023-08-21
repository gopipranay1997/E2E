#Install the below libaries before importing
import pandas as pd
# from pandas_profiling import ProfileReport
import yaml
import argparse
from evidently.report import Report
# from evidently.dashboard import Dashboard
# from evidently.dashboard.tabs import DataDriftTab,CatTargetDriftTab
from evidently.metric_preset import DataQualityPreset


def read_params(config_path):
    """
    read parameters from the params.yaml file
    input: params.yaml location
    output: parameters as dictionary
    """
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def load_data(data_path):
    """
    load csv dataset from given path
    input: csv path
    output:pandas dataframe
    """
    df = pd.read_csv(data_path, sep=",", encoding='utf-8')
    return df

def eda(config_path):
    """
    Perform EDA
    """
    config=read_params(config_path)
    # raw_data_path = config["raw_data_config"]["raw_data_csv"]
    external_data_path=config["external_data_config"]["external_data_csv"]

    df=load_data(external_data_path)
    # profile = ProfileReport(df, explorative=True)
    eda_report = Report(metrics=[DataQualityPreset()])
    #Saving results to a HTML file
    eda_report.run(current_data=df,reference_data=None)
    eda_report.save_html("./reports/templates/eda_report.html")

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    eda(config_path=parsed_args.config)


