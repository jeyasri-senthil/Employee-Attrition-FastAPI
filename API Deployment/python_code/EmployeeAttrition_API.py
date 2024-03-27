"""
Created on Wed Mar 27 16:27:23 2024

@author: jeyasri
"""


import json
import pickle
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class model_input(BaseModel):
    SatisfactionLevel : float
    LastEvaluation : float
    ProjectCount : int
    AverageMonthlyHours : int
    TimeSpent : int
    WorkAccident : int
    PromotionLast_5Years : int
    Salary : int
    
# loading the saved model
model = pickle.load(open('employee_attrition.sav', 'rb'))

@app.post('/employee_attrition')
def attrition_prediction(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    satisfyLevel = input_dictionary['SatisfactionLevel']
    lastEvaluation = input_dictionary['LastEvaluation']
    projectCount = input_dictionary['ProjectCount']
    avgMonthHours = input_dictionary['AverageMonthlyHours']
    timeSpent = input_dictionary['TimeSpent']
    workAccident = input_dictionary['WorkAccident']
    promotionGiven = input_dictionary['PromotionLast_5Years']
    salary = input_dictionary['Salary']
    
    input_list = [satisfyLevel, lastEvaluation, projectCount, avgMonthHours, timeSpent, workAccident, promotionGiven, salary]
    
    prediction = model.predict([input_list])
    
    if(prediction[0] == 0):
        return "The employee is still working in the organization."
    else: 
        return "The employee left the organization."