# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 12:33:55 2022

@author: Mark Odhiambo

Learning handling apis
"""

import requests
import json 

response=requests.get('http://127.0.0.1:5000')

print(response)