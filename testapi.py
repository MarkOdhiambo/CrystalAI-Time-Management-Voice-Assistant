# -*- coding: utf-8 -*-
"""
@author: Mark Odhiambo

Learning handling apis and testing crystal api
"""

import requests

#Cheking the status of the connection
response=requests.get('https://ninjaslayer.pythonanywhere.com/todos').json()
#print(response)

# #Checking the values in the todos
# response01=requests.get('http://127.0.0.1:5000/todos').json()
# # print(response01)

# #Putting values in the todos
# variable="Remember the milk"
# requests.post('https://ninjaslayer.pythonanywhere.com/todos', data={'task': variable}).json()
# response02=requests.get('http://127.0.0.1:5000/todos').json()

# #Checking the values in the todos
response01=requests.get('https://ninjaslayer.pythonanywhere.com/remainder'+"/"+"2022-11-23").json()
print(response01)