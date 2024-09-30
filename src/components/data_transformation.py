import os 
import sys
from src.exception import CustomException
from src.logger import logging


from sklearn.preprocessing import StandardScaler,OneHotEncoder,OrdinalEncoder,LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


from dataclasses import dataclass
import pandas as pd
import numpy as np

from src.utils import save_object



@dataclass
class DataTransformationConfig:
     preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()


    def get_data_transformer_object(self):
        try:
            
            numerical_columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar','chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density','pH', 'sulphates', 'alcohol']

            categorical_columns = ['type']


            num_pipeline = Pipeline(steps=[
                ('Imputer',SimpleImputer(strategy="median")),
                ('Standization',StandardScaler())
            
            ])
            
            cate_pipeline = Pipeline(steps=[
                ('Imputer',SimpleImputer(strategy='most_frequent')),
                ('OneHotting',OneHotEncoder(handle_unknown='ignore')),
                ('standarization',StandardScaler(with_mean=False))
                ])


            logging.info(f"Numerical columns Standard Scaling completed {numerical_columns}")
            logging.info(f'Categorical columns encoding completed {categorical_columns}')


            preprocessor = ColumnTransformer(transformers=
            [
               ("num_pipeline",num_pipeline,numerical_columns),
               ("cate_pipeline",cate_pipeline,categorical_columns), 
            ])

            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)
            

    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('Read Train and Test data is completed.')
            logging.info('Obtaining preprocessing object')

            preprocessor_obj = self.get_data_transformer_object()

            target_column_name = 'quality'

            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df = train_df[target_column_name]


            input_feature_test_df = test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df = test_df[target_column_name]


            logging.info("Applying preprocessing object on trainig dataframe and testing dataframe")


            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)
            
            train_arr = np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr,np.array(target_feature_test_df)]


            logging.info('Saved preprocessing object')

            save_object(file_path=self.data_transformation_config.preprocessor_obj_file_path,
            obj=preprocessor_obj)


            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )







        except Exception as e:
            raise CustomException(e,sys)
    