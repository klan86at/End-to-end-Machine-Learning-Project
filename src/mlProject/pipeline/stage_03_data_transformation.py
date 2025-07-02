from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger
from pathlib import Path


STAGE_NAME = "Data Transformation"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data = data_transformation.get_data()
                train, test = data_transformation.split_data(data)
                data_transformation.save_data(train, test)
            else:
                raise Exception("Data validation failed- schema not valid. Cannot proceed with data transformation.") 
        except Exception as e:
            print(e)


if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nX==========X")
    except Exception as e:
        logger.exception(e)
        raise e
    
# This code is part of a data transformation pipeline in a machine learning project.