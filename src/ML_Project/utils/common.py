import os
import yaml
import json
import joblib
from typing import Any
from pathlib import Path
from box import ConfigBox
from ML_Project import logger
from ensure import ensure_annotations
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ Read yaml file and return
    
    args: 
        path_to_yaml (str): path like input
    raises: 
        ValueError: if yaml file is empty
        e: empty file
    Return:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories  : list, verbose = True):
    """
    Create list of directories

    Args:
        path_to directories (list): list of path of directories 
        ignore_log (bool, optional): ignore if multiple directories are to be created, Default is False
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    save json data

    Args:
        path(path): path to json file
        data(dict): data to be saved in json file
    """

    with open(path,"w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at; {path}")



@ensure_annotations
def load_json(path: Path)->ConfigBox:
    """
    Load json file data

    args:
        path(Path): path to json file
    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)
    logger.info("json file loaded successfully from: {path}")

    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """"
    save binary file

    Args:
        data(Any): data to be saved as binary
        path(Path): path to binary file
    """

    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary data
    Args:
        path(Path): path to binary file
    Returns:
        Any: Object stored in the file
    """

    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get size in KB
    Args:
        path(Path): path of the file
    Returns:
        str: size in KB
    """
    size_in_kb =    round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"