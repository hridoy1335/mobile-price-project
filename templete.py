import os
import logging
from pathlib import Path


project_name = "mobile"

list_of_file = [
    f"github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_preprocessing.py",
    f"src/{project_name}/components/model_trainner.py",
    f"src/{project_name}/components/model_evaluator.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/constants/config.py",
    f"src/{project_name}/exception/__init__.py",
    f"src/{project_name}/exception/exceptions.py",
    f"src/{project_name}/logger/__init__.py",
    f"src/{project_name}/logger/logger.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/file_util.py",
    "config/config.yaml",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "app.py",
    "setup.py",
    "main.py"
]
for file in list_of_file:
    filepath = Path(file)
    filedir,filename = os.path.split(filepath)
    
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
        
    else:
        logging.info(f"file is already exist {filepath}")
        
        
print("OK")