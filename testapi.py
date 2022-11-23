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
TODOS = [
    {'id':1,'task': 'Build an API'},
    {'id':2,'task': 'Write my documentation'},
    {'id':3,'task': 'Profit!'}
]
