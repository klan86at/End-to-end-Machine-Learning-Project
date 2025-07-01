# Importing Libraries
import os
import pandas as pd
from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig

# Data Validation
class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_data(self)-> bool:
        try:
            validation_status = None
            
            data = pd.read_csv(self.config.unzip_data_dir)
            all_columns = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_columns:
                if col not in all_schema:
                    logger.error(f"Column {col} is not in the schema.")
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
            return validation_status
        
        except Exception as e:
            raise e