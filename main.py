# from src.logger import Logger
# from src.exception import CustomException
from src.utils.file_util import load_mongoDB

data = load_mongoDB()
print(data.shape)