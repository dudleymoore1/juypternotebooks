#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 11:36:18 2021

@author: dudleymoore
"""


import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
import pandas as pd
#%matplotlib inline

usa = gpd.read_file('States 21basic/geo_export_29302501-c06c-43d7-8ef0-e3f008fccd63.shp')

null_Color = "#29ff4d"
tie_Color = "#806d4b"

tilt_R = "#ffc0cb"
lean_R ="#FF0000"
safe_R = "#8B0000"

tilt_B = "#87CEFA"
lean_B ="#00BFFF"
safe_B = "#0000FF"
def state_Plotter(states, us_map = True):
    

    fig, ax = plt.subplots(figsize=(30, 30))
 
    if us_map: #Executes if us_map is set to true.
        if 'HI' in states:
            usa[0:50].plot(ax=ax, alpha = 0.3)
            
        elif 'AK' in states:
            usa[1:51].plot(ax=ax,alpha = 0.3)
            
        elif 'AK' and 'HI' in states:
            usa[0:51].plot(ax = ax, alpha = 0.3)
            
        else:
            usa[1:50].plot(ax=ax, alpha = 0.3)
            
        for n in states:
            usa[usa.state_abbr == f'{n}'].plot(ax=ax, edgecolor = 'y', linewidth = 2)
            
    elif us_map == False:
        for n in states:
            usa[usa.state_abbr == f'{n}'].plot(ax=ax, edgecolor = 'y', linewidth = 2)
    
##list_Of_States = states = ["AL", "AK",  "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI",
#           "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
#          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
#          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
#          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
#

#plt.show()