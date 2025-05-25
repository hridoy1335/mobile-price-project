import os
import sys
import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
mongodb_uri = os.getenv('MONGODB_URI')

def load_mongoDB():
    try:
        clint = MongoClient(mongodb_uri)
        db = clint['mobileDB']
        collection = db['mobileDataset']
        df = pd.DataFrame(list(collection.find()))
        return df
    except Exception as e:
        raise Exception(e,sys) from e