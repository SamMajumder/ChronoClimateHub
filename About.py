<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 10:40:51 2023

@author: samba
"""

import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Planet Pulse",
    page_icon="🌍",
)

# Title and Welcome Message
st.write("# Welcome to Planet Pulse! 🌍")

# Sidebar message
st.sidebar.success("Timelapse Videos")

# About content
st.markdown(
    """
    Planet Pulse is a dynamic platform showcasing timelapse videos that capture the pulse of our planet. Through these visual narratives, witness the changes in temperature, precipitation, biodiversity, air quality, and more, across different regions of the world.
    
    **👈 Navigate to 'Timelapse Videos' in the sidebar** to explore the visual chronicles of our changing planet.
    """
)

# Create two columns for side-by-side display
col1, col2 = st.columns(2)

# Direct raw GitHub URLs for the videos
Aerosol_video_url = 'https://raw.githubusercontent.com/SamMajumder/ChronoClimateHub/main/Timelapse_Videos/Aerosol_timelapse.mp4'
SO2_video_url = 


# Display the Aerosol timelapse video in the first column
with col1:
    st.video(Aerosol_video_url)
    st.write("Monthly absorbing aerosol index variaitons in Delhi")  # Caption below the video

# Display the SO2 timelapse video in the second column
with col2:
    st.video(SO2_video_url)
    st.write("Monthly SO2 variations in New York")  # Caption below the video





