# End-to-end-Machine-Learning-Project

## About
This project predicts wine quality (on a scale of 0–10) using physicochemical features like acidity, pH, and alcohol content. The model leverages Elastic Net regression to balance feature selection (L1 regularization) and multicollinearity handling (L2 regularization), achieving optimal performance.
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

## Overview

The 'End-to-end-Machine-Learning-Project' offers a comprehensive, production-ready template for building, tracking, and deploying machine learning models. It meticulously outlines the entire ML lifecycle, from initial configuration and data ingestion (as seen in `config/config.yaml`, `artifacts/data_ingestion`) through to a fully containerized application deployed in the cloud. This project is engineered with robust MLOps practices at its core, leveraging MLflow and Dagshub for sophisticated experiment tracking, model versioning, and remote artifact management.

At its core, the project champions an automated CI/CD pipeline, executed via GitHub Actions, which meticulously handles everything from building Docker images (as defined by `Dockerfile`) and pushing them to AWS ECR, to deploying the final containerized application onto an AWS EC2 instance. This robust setup, combined with structured project components (`src/mlProject`), dedicated research notebooks (`research/`), and a functional web interface (`app.py`, `templates/`), ensures a seamless transition from experimentation to a scalable, production-grade application. It is purpose-built for machine learning engineers and data scientists who seek a clear, repeatable, and automated pathway to deploy their models reliably into real-world production environments.

## ✨ Features

*   🚀 **End-to-End ML Lifecycle:** Offers a comprehensive template covering development, tracking, and scalable deployment of ML models.
*   📊 **MLOps with MLflow & Dagshub:** Integrates MLOps practices for robust experiment tracking and remote model management.
*   ☁️ **Automated AWS CI/CD:** Features a powerful CI/CD pipeline via GitHub Actions for seamless deployment to AWS ECR and EC2 instances.
*   🐳 **Containerized & Scalable Deployment:** Utilizes Docker for building and deploying containerized machine learning applications.
*   🏗️ **Modular ML Workflow:** Employs a structured `src` directory with components and pipelines for maintainable and configurable ML development.
*   ⚙️ **Declarative Configuration:** Manages project settings, parameters, and data schemas using `config.yaml`, `params.yaml`, and `schema.yaml`.
*   🧠 **Interactive Research & Development:** Provides Jupyter notebooks to guide through data ingestion, validation, transformation, training, and evaluation stages.

## 📦 Installation

```bash
git clone https://github.com/klan86at/End-to-end-Machine-Learning-Project.git
cd End-to-end-Machine-Learning-Project
```

## 🚀 Quick Start

To quickly get started with this project:

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/End-to-end-Machine-Learning-Project.git
    cd End-to-end-Machine-Learning-Project
    ```
2.  Set up a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
3.  Execute the end-to-end ML pipeline, which processes data and trains a model, tracking experiments with MLflow/Dagshub:
    ```bash
    python main.py
    ```
4.  Launch the prediction web application for inference:
    ```bash
    python app.py
    ```
    Access the application at `http://127.0.0.1:5000` in your web browser.

## 📁 Project Structure

```
End-to-end-Machine-Learning-Project/
├── artifacts
│   └── data_ingestion
│       ├── data.zip
│       └── winequality-red.csv
├── config
│   └── config.yaml
├── research
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_validation.ipynb
│   ├── 03_data_transformation.ipynb
│   ├── 04_model_trainer.ipynb
│   ├── 05_model_evaluation.ipynb
│   └── trials.ipynb
├── src
│   └── mlProject
│       ├── components
│       │   ├── __init__.py
│       │   ├── data_ingestion.py
│       │   ├── data_transformation.py
│       │   ├── data_validation.py
│       │   ├── model_evaluation.py
│       │   └── model_trainer.py
│       ├── config
│       │   ├── __init__.py
│       │   └── configuration.py
│       ├── constants
│       │   └── __init__.py
│       ├── entity
│       │   ├── __init__.py
│       │   └── config_entity.py
│       ├── pipeline
│       │   ├── __init__.py
│       │   ├── prediction.py
│       │   ├── stage_01_data_ingestion.py
│       │   ├── stage_02_data_validation.py
│       │   ├── stage_03_data_transformation.py
│       │   ├── stage_04_model_trainer.py
│       │   └── stage_05_model_evaluation.py
│       ├── utils
│       │   ├── __init__.py
│       │   └── common.py
│       └── __init__.py
├── templates
│   ├── index.html
│   └── results.html
├── .dvcignore
├── .gitignore
├── Dockerfile
├── README.md
├── app.py
├── clean-joblib.sh
├── main.py
├── params.yaml
├── requirements.txt
├── requirements_backup.txt
├── schema.yaml
└── template.py
```

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

1. Fork the repository at [https://github.com/klan86at/End-to-end-Machine-Learning-Project.git](https://github.com/klan86at/End-to-end-Machine-Learning-Project.git)
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

## 📄 License

This project is open source. See the [LICENSE](LICENSE) file for details.
