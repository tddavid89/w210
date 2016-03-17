# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 07:25:42 2016

@author: tdavid
"""

import pandas as pd
import numpy as np

dt = pd.read_csv('/Users/tdavid/Documents/MIDS/w210/dataset-examples-master/yelp_academic_all.csv',sep=",")

###############
# Restaurants #
###############
rest_list = list()
for i in range(0,len(dt)):
    try:
        if 'Restaurants' in dt.business_categories[i]:
            rest_list.append(i)
    except:
        continue


dt_rest = dt.ix[rest_list]
dt_rest = dt_rest.reset_index(drop=True)

###########
# Arizona #
###########
az_list = list()
for i in range(0,len(dt)):
    try:
        if 'AZ' in dt.state[i]:
            az_list.append(i)
    except:
        continue
    
dt_final = dt_rest.ix[az_list]
dt_final = dt_final.reset_index(drop=True)


############################
# GROUP SCORES BY BUSINESS #
############################