import yaml
import argparse
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def read_params(config_path):
    """
    read parameters from the params.yaml file
    input: params.yaml location
    output: parameters as dictionary
    """
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def load_data(data_path,model_var):
    """
    load csv dataset from given path
    input: csv path
    output:pandas dataframe
    """
    df = pd.read_csv(data_path, sep=",", encoding='utf-8')
    df=df[model_var]
    return df

def preprocess(config_path):
    """
    load data from external location(data/external) to the raw folder(data/raw) with train and testing dataset 
    input: config_path
    output: save train file in data/raw folder
    """
    config=read_params(config_path)
    external_data_path=config["external_data_config"]["external_data_csv"]
    raw_data_path=config["raw_data_config"]["raw_data_csv"]
    model_var=config["raw_data_config"]["model_var"]
    processed_data_path = config["processed_data_config"]["processed_data_csv"]


    raw_df=load_data(raw_data_path,model_var)
    """Add some preprocessing here"""
    raw_df=pd.get_dummies(raw_df,drop_first=True)
    raw_df.to_csv(processed_data_path,index=False)

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    preprocess(config_path=parsed_args.config)