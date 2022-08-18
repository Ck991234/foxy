import streamlit as st
import pandas as pd
import numpy as np
import geocoder

url = "https://github.com/Ck991234/foxy/blob/0a27593660add05b10b01230863c07e591328aee/zomatogeo.csv?raw=true"

st.title('Pune Hotel Recommendation Engine')

location = st.text_input('Type Any Pune Location')

#Geo Location Extractor
def get_geolocation (place):
    g = geocoder.arcgis(str(place) +","+"Pune")
    return g.latlng
    
latlog = get_geolocation(location)
st.write('Your Geo Location Is ',latlog[0],latlog[1])

#KNN Algorithem 
@st.cache
def topt(lattitude,longitude):
    df = pd.read_csv(url,index_col=0)
    inlattitude = lattitude * np.pi/180
    inlongitude = longitude * np.pi/180
    df["e_distance"] = np.sqrt(((inlattitude - df["rad_latit"] )**2) + ((inlongitude - df["rad_longi"])**2))
    df2 = {'Restaurant_Name': 'My Current Location', 'longitude': longitude, 'lattitude':lattitude, 'e_distance':0  }
    df1 = df.append(df2, ignore_index = True)
    final_data = df1.sort_values(["e_distance"],ascending=True).head(10)
    final_data. rename(columns = {'longitude':'lon', 'lattitude':'lat'}, inplace = True)
    return final_data 
top_20 = topt(latlog[0],latlog[1])
st.write(top_20["Restaurant_Name"])
st.map(data = top_20, zoom=None, use_container_width=True)


