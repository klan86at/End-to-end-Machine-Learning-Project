# Importing necessary libraries and modules.
import os
import pandas as pd
import joblib
from mlProject import logger
from sklearn.linear_model import ElasticNet
from mlProject.config.configuration import ModelTrainerConfig


# Implementing model trainer component
class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        logger.info("Loading training data")
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        logger.info("Training model")
        model = ElasticNet(
            alpha=self.config.alpha,
            l1_ratio=self.config.l1_ratio,
            random_state=42
        )

        X_train = train_data.drop(columns=[self.config.target_column])
        X_test = test_data.drop(columns=[self.config.target_column])
        y_train = train_data[self.config.target_column]
        y_test = test_data[self.config.target_column]

        model.fit(X_train, y_train)


        # Save model
        logger.info("Saving model")
        model_file_path = os.path.join(self.config.root_dir, self.config.model_name)
        
        # Create directory
        try:
            os.makedirs(os.path.dirname(model_file_path), exist_ok=True)
            joblib.dump(model, model_file_path)
        except Exception as e:
            logger.error(f"Failed to save model: {str(e)}")
            raise
        
        logger.info(f"Model saved to {model_file_path}")
