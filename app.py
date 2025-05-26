import sys
from src.logger.logger import logging
from src.exception.exceptions import CustomException
from src.components.data_ingestion import (DataIngestion,
                                           DataIngestionConfig)
from src.components.data_preprocessing import (DataTransformation,
                                               DataTransformationConfig)
if __name__ == "__main__":
    try:
        logging.info('data ingestion is going on.')
        
        # data_ingeston_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        train_data,test_data=data_ingestion.initiate_data_ingestion()
        
        logging.info('data preprossesing is going on.')
        
        # data_transformation_config = DataTransformationConfig()
        data_transformation = DataTransformation()
        data_transformation.initiate_data_transformation(train_data,test_data)
        
    except Exception as e:
        raise CustomException(e,sys)