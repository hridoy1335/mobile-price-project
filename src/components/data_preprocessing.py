import sys
import numpy as np
import pandas as pd
from dataclasses import dataclass
from src.constants.config import *
from src.logger.logger import logging 
from src.utils.file_util import save_object
from src.exception.exceptions import CustomException
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file = PREPROSSESOR_OBJECT


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        
    def get_data_transformation_object(self):
        try:
            logging.info('Data preprocessing is starting.')
            
            numerical_columns = [[
                'battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g',
                'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height',
                'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time', 'three_g',
                'touch_screen', 'wifi'
            ]]
            logging.info(f"Defined {len(numerical_columns)} numerical columns.")
            
            num_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ])
            
            logging.info('Numerical pipeline built successfully.')
            
            preprocessor = ColumnTransformer([
                ('num_pipeline', num_pipeline, numerical_columns)
            ])
            
            return preprocessor
            
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            logging.info('Initiating data transformation.')
            
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)
            
            logging.info(f'Train data shape: {train_data.shape}, Test data shape: {test_data.shape}')
            
            preprocessor_obj = self.get_data_transformation_object()
            
            logging.info('Preprocessor object created successfully.')
            
            target_feature = "price_range"
            
            input_feature_train_data = train_data.drop(columns=[target_feature], axis=1)
            target_feature_train_data = train_data[target_feature]
            
            input_feature_test_data = test_data.drop(columns=[target_feature], axis=1)
            target_feature_test_data = test_data[target_feature]
            
            logging.info('Split train and test data into input and target features.')
            
            logging.info('Applying preprocessing to training and testing data.')
            
            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_data)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_data)
            
            train_array = np.c_[input_feature_train_arr, np.array(target_feature_train_data)]
            test_array = np.c_[input_feature_test_arr, np.array(target_feature_test_data)]
            
            logging.info('Saving preprocessor object to file.')
            
            save_object(
                filepath=self.data_transformation_config.preprocessor_obj_file,
                obj=preprocessor_obj
            )
            
            return (
                train_array,
                test_array,
                self.data_transformation_config.preprocessor_obj_file
            )
            
        except Exception as e:
            raise CustomException(e, sys)
