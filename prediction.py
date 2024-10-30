import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from imblearn.combine import SMOTEENN



ordinal_cols = ['BMI_Category', 'AgeCategory', 'Race', 'GenHealth']
boolean_cols = ['HeartDisease', 'Smoking', 'AlcoholDrinking', 'Stroke', 
                'DiffWalking', 'Diabetic', 'PhysicalActivity', 'Asthma', 
                'KidneyDisease', 'SkinCancer']

ordinal_mappings = {
    'BMI_Category': ['Underweight', 'Normal weight', 'Overweight', 
                     'Obesity I', 'Obesity II', 'Obesity III'],
    'AgeCategory': ['18-24', '25-29', '30-34', '35-39', '40-44', 
                    '45-49', '50-54', '55-59', '60-64', '65-69', 
                    '70-74', '75-79', '80 or older'],
    'Race': ['White', 'Black', 'Asian', 'Hispanic', 
             'American Indian/Alaskan Native', 'Other'],
    'GenHealth': ['Poor', 'Fair', 'Good', 'Very good', 'Excellent']
}


def create_preprocessor():
    preprocessor = ColumnTransformer(
        transformers=[
            ('ord', OrdinalEncoder(categories=[ordinal_mappings[col] for col in ordinal_cols]), ordinal_cols),  
            ('ohe', OneHotEncoder(drop='first'), boolean_cols) 
        ],
        remainder='passthrough'  
    )
    return preprocessor

def predict_with_model(model, input_data):
   
    preprocessor = create_preprocessor()

    
    input_transformed = preprocessor.fit_transform(input_data)

 
    scaler = StandardScaler()
    input_scaled = scaler.fit_transform(input_transformed)

    
    predictions = model.predict(input_scaled)
    return predictions


def predict(input_data):
   
    model = lgb.Booster(model_file='C:\GitHub\SDS3787-Lab-Groupe-5\lightgbm_model.txt')
    return predict_with_model(model, input_data)

dataframe = pd.DataFrame({
    "BMI_Category": ['Obesity II'],
    "AgeCategory": ["55-59"],
    "Race": ["Hispanic"],
    "GenHealth": ["Fair"],
    "HeartDisease": [0],
    "Smoking": [0],
    "AlcoholDrinking": [0],
    "Stroke": [0],
    "DiffWalking": [0],
    "Diabetic": [1],
    "PhysicalActivity": [1],
    "Asthma": [0],
    "KidneyDisease": [1],
    "SkinCancer": [0]                 
})

predict(dataframe)