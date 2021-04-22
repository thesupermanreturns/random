# -*- coding: utf-8 -*-


# We can try this using postman also

import requests

url = "http://localhost:5000/api_predict"
data = {
        "sepal_length" : 10,
        "sepal_width":0.1,
         "petal_length":0,
         "petal_width":10
        
        }

r = requests.post(url, json = data)
print(r)
print(r.text)

