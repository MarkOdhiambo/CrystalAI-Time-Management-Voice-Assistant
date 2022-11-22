# -*- coding: utf-8 -*-
"""
@author: Mark Odhiambo

Learning handling apis and testing crystal api
"""

import requests
import json 

#Cheking the status of the connection
response=requests.get('http://127.0.0.1:5000/todos')
# print(response)

#Checking the values in the todos
response01=requests.get('http://127.0.0.1:5000/todos').json()
# print(response01)

#Putting values in the todos
variable="Remember the milk"
requests.post('http://127.0.0.1:5000/todos', data={'task': variable}).json()
response02=requests.get('http://127.0.0.1:5000/todos').json()
print(response02)
for todo in response02:
    print(todo['task'])
