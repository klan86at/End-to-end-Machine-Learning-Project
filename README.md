# End-to-end-Machine-Learning-Project

## Workflows
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py


How to Run

## STEPS
clone the repository

```bash
https://github.com/klan86at/End-to-end-Machine-Learning-Project.git
```
## STEP 01 create a conda enviroment after opening repository

```bash
conda create -n myenv python=3.12 -y
```
```bash
conda activate myenv
```

## STEP 02 Install the requirements.txt

```bash
pip install -r requirements.txt
```

```bash
# Run the following command
python app.py
```

Now,
```bash
open up your local host & port
```
## MLFLOW
[documentation](https://mlflow.org/docs/latest/index.html)

#### cmd
-mlflow ui

## dagshub
[dagshub](https://dagshub.com/)
MLFLOW_TRACKING_URI=https://dagshub.com/klan86at/End-to-end-Machine-Learning-Project.mlflow \
MLFLOW_TRACKING_USERNAME=klan86at \
MLFLOW_TRACKING_PASSWORD=332b51719afa1eb8c7b19f01b95fd0d1def95031 \
python script.py

Run this to export as env variables:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/klan86at/End-to-end-Machine-Learning-Project.mlflow

export MLFLOW_TRACKING_USERNAME=klan86at

export MLFLOW_TRACKING_PASSWORD=332b51719afa1eb8c7b19f01b95fd0d1def95031

```
