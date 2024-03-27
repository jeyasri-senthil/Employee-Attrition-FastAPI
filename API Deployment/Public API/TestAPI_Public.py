"""
Created on Wed Mar 27 18:02:39 2024

@author: jeyasri
"""


import json
import requests

url = 'https://379d-104-196-126-65.ngrok-free.app/employee_attrition'

input_data_for_model = {
    'SatisfactionLevel' : 0.86,
    'LastEvaluation' : 0.99,
    'ProjectCount' : 3,
    'AverageMonthlyHours' : 169,
    'TimeSpent' : 2,
    'WorkAccident' : 1,
    'PromotionLast_5Years' : 0,
    'Salary' : 1
    }

input_json = json.dumps(input_data_for_model)
response = requests.post(url, data = input_json)
print(response.text)