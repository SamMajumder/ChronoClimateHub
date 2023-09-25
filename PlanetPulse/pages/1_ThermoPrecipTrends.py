# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 10:47:14 2023

@author: samba
"""

# Import necessary libraries
import streamlit as st

st.set_page_config(page_title="ThermoPrecipTrends: Temperature & SPEI Changes in the Contiguous US")

st.markdown("# ThermoPrecipTrends: Temperature & SPEI Changes in the Contiguous US")

st.sidebar.header("ThermoPrecipTrends")


#### Introduction

st.write("""
    This page contains two timelapse videos. One showcasing the change in temperature across the contiguous United States between 1960 and 2023.
    The other pertains to the shifts in Standardized Precipitation Evapotranspiration Index (SPEI) during the same period. 
    """
   )

# Create two columns for side-by-side display
col1, col2 = st.columns(2)

# Display the temperature timelapse video in the first column
with col1:
    temp_video_file = open('C:/Users/samba/Documents/ChronoClimateHub/Timelapse_videos/temperature_timelapse.mp4', 'rb')
    temp_video_bytes = temp_video_file.read()
    st.video(temp_video_bytes)
    st.write("Temperature Timelapse")  # Caption below the video

    # Display SPEI Data Information below the temperature video in the first column
    
    

# Display the SPEI timelapse video in the second column
with col2:
    spei_video_file = open('C:/Users/samba/Documents/ChronoClimateHub/Timelapse_videos/Spei_timelapse.mp4', 'rb')
    spei_video_bytes = spei_video_file.read()
    st.video(spei_video_bytes) 
    st.write("SPEI Timelapse")  # Caption below the video



# Data Source Information
st.subheader("Data Source")
st.write("""
The temperature data for this project is sourced from the National Centers for Environmental Information (NCEI). 
It is part of the NCLIMGRID product, provides monthly temperature averages across the contiguous US. 
It's a valuable resource for understanding long-term temperature trends and variations.
""")

st.markdown("[Link to the temperature dataset](https://www.ncei.noaa.gov/data/nclimgrid-monthly/access/)") 

st.write("""
The SPEI data for this project is sourced from the National Centers for Environmental Information (NCEI). 
SPEI is an index that quantifies drought by considering both precipitation and potential evapotranspiration. 
It provides a measure of water availability and drought severity.
    """)
st.markdown("[More information about SPEI](https://journals.ametsoc.org/view/journals/clim/23/7/2009jcli2909.1.xml?tab_body=pdf)")
st.markdown("[Additional SPEI Info](https://climatedataguide.ucar.edu/climate-data/standardized-precipitation-evapotranspiration-index-spei)")
st.markdown("[Link to Dataset](https://www.ncei.noaa.gov/pub/data/nidis/indices/nclimgrid-monthly/spei-pearson/nclimgrid-spei-pearson-01.nc)")


# Data Processing and Calculation
st.subheader("Data Processing and Calculation: Temperature and SPEI")
st.write("""
The data processing involves the following steps:
- Data Acquisition: Data from netCDF files, which is commonly used for storing large-scale environmental data, were acquired using R. 
We are only woring with the data which spans from the year 1960 to 2023.
- Data Cleaning: The raw data was subset to include only the relevant layers, specifically from 781 through the end of the dataset. 
This ensured that we focused on the time frame of interest.
- Data Processing: The dataset provides monthly temperature data. To simplify and provide a clearer trend, yearly average temperatures 
were calculated for each year. This was achieved by averaging the monthly data for each year. 

R Packages used in this project are progress, transformr, gganimate, raster, ncdf4, tidyverse suite of packages

""")



     
        
        