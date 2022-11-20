# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 12:33:55 2022

@author: Mark Odhiambo

Learning handling apis
"""

import requests
import json 

response=requests.get('https://api.stackexchange.com/2.3/answers?order=desc&sort=activity&site=stackoverflow')

print(response)