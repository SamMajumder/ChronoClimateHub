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

