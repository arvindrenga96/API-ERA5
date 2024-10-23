#!/usr/bin/env python
# coding: utf-8

import os
from IPython.display import HTML
from IPython.display import display
import api_func_ag
from datetime import datetime, timedelta
from netCDF4 import Dataset
import numpy as np
import xarray as xr

# Pre-requirements
udi = '83f26bcf-91c9-4570-bfbc-aceb220f80a7'
key = 'e6487f45-a948-4134-b1e0-4d8087f87c73' 

path = '/home/kumarv/renga/Documents/Fall_24/API-ERA5/Data'

#Variable, time period and geographical location
variables = [
    "precipitation_flux", "solar_radiation_flux", "2m_temperature", "2m_dewpoint_temperature"
]

# variables = [
#      "2m_temperature", "2m_dewpoint_temperature"
# ]

# years = years = ['2001']
years = years = [
    '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010',
    '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020',
    '2021', '2022', '2023', '2024'
]  # You can add more years if needed
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
days = 'all'
hours = 'all'

# Boundaries of the geographical area in decimal degrees
north_boundary = 90
south_boundary = -90
east_boundary = 180
west_boundary = -180

# Create CDS file
api_func_ag.make_cds_file(key, path)

# Iterate through each month
for year in years:
    for month in months:
        filename = f'era5_data_{year}_{month}'
        
        print(f"Downloading data for {year}-{month}")
        
        api_func_ag.return_cdsbeta(
            filename, 
            variables, 
            [year], 
            [month], 
            days, 
            hours,  
            [north_boundary, west_boundary, south_boundary, east_boundary]
        )
        
        print(f"Download complete for {year}-{month}")

print("All downloads completed.")

# You can add code here to visualize your variables if needed