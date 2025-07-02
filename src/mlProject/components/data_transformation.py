# Importing necessary libraries
import os
import pandas as pd
import numpy as np
from mlProject import logger
from sklearn.model_selection import train_test_split
from mlProject.entity.config_entity import DataTransformationConfig

# Setting up data transformation class
class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def get_data(self) -> pd.DataFrame:
        data = pd.read_csv(self.config.data_path)
        return data

    def split_data(self, data: pd.DataFrame) -> tuple:
        train, test = train_test_split(data, test_size=0.2, random_state=42)

        logger.info(f"Split data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)

        return train, test

    def save_data(self, train: pd.DataFrame, test: pd.DataFrame):
        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)

        logger.info(f"Saved train and test data to {self.config.root_dir}")