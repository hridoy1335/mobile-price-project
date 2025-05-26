import os
import sys
import pandas as pd
from dataclasses import dataclass
from src.constants.config import *
from src.logger.logger import logging
from src.utils.file_util import load_mongoDB
from src.exception.exceptions import CustomException
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig():
    raw = RAW_DATA_PATH
    test = TEST_DATA_PATH
    train = TRAIN_DATA_PATH
    
class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self)->pd.DataFrame:
        try:
            logging.info('loading the data from mongodb database')
            # data = load_mongoDB()
            data = pd.read_csv(os.path.join('notebook/data','raw.csv'))
            df = data
            
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw),exist_ok=True)
            df.to_csv(self.data_ingestion_config.raw,index=False,header=True)
            logging.info(f'the raw data is loaded successfully:-:{df.shape}')
            
            train_data, test_data = train_test_split(df,test_size=0.25,random_state=42)
            
            train_data.to_csv(self.data_ingestion_config.train,index=False,header=True)
            test_data.to_csv(self.data_ingestion_config.test,index=False,header=True)
            
            logging.info(f'train and test data spile is successfull  train data size is {train_data.shape}, test data size is {test_data.shape}')
            
            logging.info('data ingestion is seccessfully completed')
            return(
                train_data,
                test_data
            )
            
        except Exception as e:
            raise CustomException(e, sys)
        
# if __name__ == "__main__":
#     obj = DataIngestion()
#     obj.initiate_data_ingestion()
        
    

