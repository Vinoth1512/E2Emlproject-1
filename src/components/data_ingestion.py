import os
import sys     ## OS and sys is imported because we are using custom exception

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) ## adds the parent directory of the current file to the Python system path 

from exception import CustomException 
from logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

''' THIS FILE MAINLY FOR DATA INGESTION (Reading the input raw data and splitting the data into train and test)'''

@dataclass             ## Decorator
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv')    ## train data file (train.csv) stores in artifacts folder
    test_data_path: str=os.path.join('artifacts','test.csv')      ## test data file (test.csv) stores in artifacts folder
    raw_data_path: str=os.path.join('artifacts','data.csv')       ## raw data file (data.csv) stores in artifacts folder


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('C:\\Users\\vinot\\Downloads\\Vinoth\\Python\\Krish Naik\\End to End Project\\ML\\notebook\\data\\stud.csv')
            logging.info('Read the dataset as dataframe')
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info('Train Test Split Initiated')
            train_set,test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of the data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()


    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)
     
 