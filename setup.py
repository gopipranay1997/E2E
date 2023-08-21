from setuptools import find_packages, setup
from pathlib import Path
from setuptools import find_namespace_packages

# Load packages from requirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

# setup.py
setup(
    name="churn",
    version=0.1,
    description="Predicting Customer Churn",
    author="B Akhil Kumar",
    author_email="theakhilumarb@gmail.com",
    python_requires=">=3.7",
    install_requires=[required_packages],
)

# setup(
#     name='src',
#     packages=find_packages(),
#     version='0.1.0',
#     description='Predicting customer churn',
#     author='Akhil',
#     license='MIT',
# )
