import os
import sys
import pandas as pd
import pickle
from dotenv import load_dotenv
from pymongo import MongoClient
from src.constants.config import *
from src.logger.logger import logging
from src.exception.exceptions import CustomException

db_name:str = MONGO_DB_NAME
collection_name:str = MONGO_DB_COLLECTION

load_dotenv()
mongodb_uri = os.getenv('mongodb_uri')

def load_mongoDB():
    try:
        clint = MongoClient(mongodb_uri)
        db = clint[db_name]
        collection = db[collection_name]
        df = pd.DataFrame(list(collection.find()))
        return df
    except Exception as e:
        raise CustomException(e,sys)
    
def save_object(filepath,obj):
    try:
        dir_path = PREPROSSESOR_OBJECT
        os.makedirs(dir_path,exist_ok=True)
        
        with open(filepath,'wb') as file:
            pickle.dump(obj,file)
    except Exception as e:
        raise CustomException(e,sys)
        
        