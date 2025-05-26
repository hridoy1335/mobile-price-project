import os


# MongoDB data sources
MONGO_DB_NAME:str = "mobileDB"
MONGO_DB_COLLECTION:str = "mobileDataset"


# DVC configuration all sources
# DVC_MONGO_DB_NAME:str = "dvc_data"
# DVC_MONGO_DB_COLLECTION_NAME:str = "dvc_collection"


# Data Ingestion Constants Files
TRAIN_DATA_PATH:str = os.path.join('artifacts','train_data.csv')
TEST_DATA_PATH:str = os.path.join('artifacts','test_data.csv')
RAW_DATA_PATH:str = os.path.join('artifacts','raw.csv')


# Data Transformation Constants Files
PREPROSSESOR_OBJECT:str = os.path.join('artifacts','preprossesor.pkl')
# TRAIN_ARRAY:str = os.path.join('artifacts','train_array')
# TEST_ARRAY:str = os.path.join('artifacts','test_array')