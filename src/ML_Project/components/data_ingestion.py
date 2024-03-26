import os
from pathlib import Path
import zipfile
import urllib.request as request
from ML_Project import logger
from ML_Project.utils.common import get_size
from ML_Project.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(
                url = self.config.source_url,
                filename=self.config.local_data_file)
            logger.info(f"{filename} download! with following info: \n{header}")
        else:
            size_file = get_size(Path(self.config.local_data_file))
            logger.info(f"file already exists of size: {size_file}")

    def extract_zip_file(self):
        """
        zip file path : str
        extract zip file into the data directory
        function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)