import os
from pathlib import Path
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = "cnnClassification"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/artifact_entity.py",
    f"src/{project_name}/entity/config_entity.py",
    f'src/{project_name}/constants/__init__.py',
    f"src/{project_name}/constants/training_pipeline_constants.py",
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/logging/logger.py',
    f'src/{project_name}/exception/__init__.py',
    f'src/{project_name}/exception/exception.py',
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'requirements.txt',
    'setup.py',
    'research/trails.ipynb',
    'templates/index.html'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)  # Corrected here

    # Create directories if they do not exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Corrected here
        logging.info(f'Creating directory: {filedir} for the file: {filename}')

    # Create file if it does not exist or is empty
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            pass
        logging.info(f'Creating file: {filepath}')
