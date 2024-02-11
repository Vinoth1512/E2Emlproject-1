import os 
import sys

import numpy as np 
import pandas as pd
import dill  ## Help us to create pickle file

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) ## adds the parent directory of the current file to the Python system path 

from src.exception import CustomException



def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
