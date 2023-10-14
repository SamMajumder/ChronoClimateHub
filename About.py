

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
SO2_video_url = 'https://raw.githubusercontent.com/SamMajumder/ChronoClimateHub/main/Timelapse_Videos/SO2.mp4'


# Display the Aerosol timelapse video in the first column
with col1:
    st.video(Aerosol_video_url)
    st.write("Monthly absorbing aerosol index variaitons in Delhi")  # Caption below the video

# Display the SO2 timelapse video in the first column
with col2:
    st.video(SO2_video_url)
    st.write("Monthly SO2 column number density in New York")  # Caption below the video


# Data Source Information
st.subheader("Data Source")
st.write("""
The data for this project is sourced from the Copernicus Sentinel-5P satellite, courtesy of datasets COPERNICUS/S5P/NRTI/L3_AER_AI and 
"COPERNICUS/S5P/NRTI/L3_SO2". These datasets provides valuable near real time insights into the Aerosol Index (AI) and Sulphur dioxide density, 
which is instrumental in identifying the presence of absorbing aerosol particles and SO2 in the atmosphere. These datasets
encompasses global data, offering a rich resource for aerosol distribution and concentration analysis.
""")

st.markdown("[Link to the Aerosol index dataset](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_AER_AI)") 
st.markdown("[Link to the Sulphur dioxide column number density dataset](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_SO2)") 


# Data Processing and Calculation
st.subheader("Data Processing and Calculation")
st.write("""
The data processing involves the following steps:
- Data Acquisition: Data spanning from November 2018 to August 2023 was acquired via the Google Earth Engine platform. This dataset was filtered to focus 
  on two distinct geographical regions: New Delhi, India, and Staten Island, New York. Data was extracted on a monthly basis with different band names 
  specified for each location; 'absorbing_aerosol_index' for New Delhi and 'SO2_column_number_density' for Staten Island.
- Data Cleaning: The initial data was filtered to include only the relevant time frames and geographical extents to ensure a concentrated analysis on 
  the selected areas.
- Data Processing and Visualization: Custom Python functions were utilized to compute monthly mean values for the specified band in each location and were 
  used to generate monthly visualizations of the data
  

Python modules used in this project are pandas, folium, geopandas, shapely, ee, rasterio and os

""")



