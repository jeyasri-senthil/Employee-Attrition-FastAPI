"""
Created on Wed Mar 27 16:27:23 2024

@author: jeyasri
"""


import json
import requests

url = 'http://127.0.0.1:8000/employee_attrition'

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