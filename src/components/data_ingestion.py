import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
import psycopg2
from sqlalchemy import create_engine
from set_tmp_env_var import set_variables
set_variables()
engine = create_engine("postgresql://{0}:{1}@{2}:{3}/{4}".format(os.environ["DB_USER"], os.environ["DB_PASS"], os.environ["DB_HOST"], os.environ["DB_PORT"], os.environ["DB_NAME"]))
dbConnection    = engine.connect()


@dataclass
class DataIngestionConfig:
    train_data_path : str=os.path.join('artifact','train.csv')
    test_data_path : str=os.path.join('artifact','test.csv')
    raw_data_path : str=os.path.join('artifact','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config= DataIngestionConfig()

    def intiate_data_ingestion(self):
        logging.info("Entered the data ingestion methods or components")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            # df= pd.read_sql("select * from dc_partner_excel_mapping", dbConnection)
            logging.info("Read dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiate started")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    train_data,test_data=obj.intiate_data_ingestion()

    data_transformation= DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)

        



