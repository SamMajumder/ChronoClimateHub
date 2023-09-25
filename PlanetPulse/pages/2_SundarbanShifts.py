# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 09:41:04 2023

@author: samba
"""

# Import necessary libraries
import streamlit as st

st.set_page_config(page_title="SundarbanShifts: Highlighting the shifts and changes in the Sundarbans region")

st.markdown("# SundarbanShifts: Highlighting the shifts and changes in the Sundarbans region")

st.sidebar.header("SundarbanShifts")


# Introduction
st.write("""
The Sundarbans Mangroves span across Bangladesh and India and are the largest mangrove forest in the world. 
They are home to the famous Royal Bengal Tiger and are a UNESCO World Heritage Site. The region is a complex 
ecosystem comprising of mangrove forests, swamps, and tidal waterways. Monitoring the NDVI in this area is 
crucial due to its ecological importance and the threats it faces from climate change, sea-level rise, and human activities.
""")

# Display the timelapse video
video_file = open('C:/Users/samba/Documents/ChronoClimateHub/Timelapse_videos/Sundarbans_timelapse.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

# Data Source Information
st.subheader("Data Source")
st.write("""
The data for this project is sourced from the MODIS (Moderate Resolution Imaging Spectroradiometer) satellite's 
MOD13A2 product. This product provides NDVI values at a 16-day interval, which we've aggregated annually for our analysis.
The specific dataset being MODIS/006/MOD13A2
""")


# Data Processing and Calculation
st.subheader("Data Processing and Calculation")
st.write("""
The data processing involves the following steps:
- Data Extraction: We extract the MODIS NDVI data within our study period.
- Data Aggregation: The 16-day interval NDVI data is aggregated to get the mean NDVI value for each year.
- Data Visualization: The mean NDVI values are visualized on a map to show the spatial distribution of vegetation 
health in the Sundarbans. Visualize the processed data using Python libraries and tools like matplotlib and create 
a timelapse video of the change in NDVI values over time.
""")



