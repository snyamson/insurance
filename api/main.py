import joblib
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd


app = FastAPI()


# Load the saved model and preprocessor
best_model = joblib.load('best_model.joblib')
preprocessor = joblib.load('preprocessor.joblib')

# Define the request payload model
class InsuranceRequest(BaseModel):
    age: int
    sex: str
    bmi: float
    children: int
    smoker: str
    region: str


@app.get('/')
def get_root():
    return {'api': 'Insurance Premium Charge Prediction'}


@app.post("/predict")
def predict_insurance_charges(insurance_request: InsuranceRequest):
  # Transform the input data for prediction
    input_data = pd.DataFrame(insurance_request.dict(), index=[0])
    transformed_data = preprocessor.transform(input_data)

    # Make the prediction
    prediction = best_model.predict(transformed_data)
    # Return the prediction as a dictionary
    return {"prediction": prediction[0]}
    


