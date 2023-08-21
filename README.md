Customer Churn
==============================

Predicting Customer Churn

Pipeline

![Alt text](images/mlops.png "Pipeline")

<!-- ![mlops](https://www.github.com/hakunamatata1997/blob/images/mlops.png) -->

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   ├── figures        <- Generated graphics and figures to be used in reporting
    │   ├── templates      <- EDA and Data Drift reports as html
    │   ├── Dockerfile     <- Dockerfile for monitoring data drift
    │   ├── Dockerfile_eda <- Dockerfile for EDA
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │    ├── load_data.py
    │   │    ├── eda.py
    │   │    ├── preprocess.py
    │   │    ├── split_data.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── optimization.py
    │   │   ├── train_model.py
    │   │   ├── model_selection.py
    │   │   ├── model_monitor.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    ├── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
    ├── tests              <- tests for python
    ├── webapp             <- folder for hosting model in production
    ├── dvc.yaml           <- DVC pipeline stages file
    ├── Jenkinsfile        <- Jenkins Pipeline file
    ├── requirements.txt   <- requirements for running this project
    ├── params.yaml        <- parameters configuration for this project
    └── deployment         <- yaml files required for creating deployment in kubernetes


--------
