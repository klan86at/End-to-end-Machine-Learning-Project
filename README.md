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

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 343218192053.dkr.ecr.us-east-2.amazonaws.com/mlken

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app
