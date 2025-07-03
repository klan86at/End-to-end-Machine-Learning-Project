# Importing Libraries
import os
import tempfile
import time
from pathlib import Path
from dagshub.upload import Repo
import pandas as pd
import joblib
import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from urllib.parse import urlparse
from mlProject.utils.common import save_json
from mlProject.entity.config_entity import ModelEvaluationConfig



class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)

        return rmse, mae, r2
    
    def log_into_mlflow(self):
        """Windows-proof MLflow/DagsHub logging"""
        
        # 1. Load data and model
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        # 2. Set tracking URI
        tracking_uri = self.config.mlflow_uri or "file:///mlruns"
        mlflow.set_tracking_uri(tracking_uri.replace('.mlflow', '') + '.mlflow')

        with mlflow.start_run():
            # 3. Log metrics
            X_test = test_data.drop(columns=[self.config.target_column])
            y_test = test_data[self.config.target_column]
            y_pred = model.predict(X_test)
            rmse, mae, r2 = self.eval_metrics(y_test, y_pred)
            mlflow.log_metrics({"rmse": rmse, "mae": mae, "r2": r2})

            # 4. Log parameters
            mlflow.log_params(self.config.all_params)

            # 5. Save model temporarily
            temp_dir = tempfile.mkdtemp()
            temp_path = Path(temp_dir) / f"model_{time.time_ns()}.joblib"
            joblib.dump(model, temp_path)

            # 6. Log model with fallback logic
            try:
                mlflow.sklearn.log_model(model, "model")
            except Exception:
                if tracking_uri.startswith("https://"): 
                    from dagshub.upload import Repo
                    repo_name = tracking_uri.split('/')[-1].split('.')[0]
                    try:
                        Repo(
                            os.getenv('MLFLOW_TRACKING_USERNAME'),
                            repo_name,
                            token=os.getenv('MLFLOW_TRACKING_PASSWORD'),
                            branch="main"
                        ).upload(str(temp_path), "models/model.joblib")
                    except Exception as e:
                        print(f"DagsHub upload failed: {e}")
                        mlflow.log_artifact(str(temp_path))
                else:
                    mlflow.log_artifact(str(temp_path))

            # 7. Cleanup temp files with retry
            for _ in range(3):
                try:
                    temp_path.unlink()
                    Path(temp_dir).rmdir()
                    break
                except (PermissionError, FileNotFoundError):
                    time.sleep(0.5)
