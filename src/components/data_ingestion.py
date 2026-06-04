import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.utils.exception import CustomException
from src.utils.logger import logging

class DataIngestion:

   def __init__(self):

       self.train_data_path = "data/processed/train.csv"

       self.test_data_path = "data/processed/test.csv"

       self.raw_data_path = "data/raw/walmart.csv"

   def initiate_data_ingestion(self):

       logging.info("Entered Data Ingestion Method")

       try:

           df = pd.read_csv(self.raw_data_path)

           logging.info("Dataset Read Successfully")

           os.makedirs(
               os.path.dirname(self.train_data_path),
               exist_ok=True
           )

           train_set, test_set = train_test_split(
               df,
               test_size=0.2,
               random_state=42
           )

           train_set.to_csv(
               self.train_data_path,
               index=False,
               header=True
           )

           test_set.to_csv(
               self.test_data_path,
               index=False,
               header=True
           )

           logging.info("Data Ingestion Completed")

           return (
               self.train_data_path,
               self.test_data_path
           )

       except Exception as e:

           raise CustomException(e, sys)
