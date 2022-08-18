<<<<<<< HEAD
import streamlit as st
import pandas as pd
import numpy as np
url = "https://github.com/Ck991234/foxy/blob/0a27593660add05b10b01230863c07e591328aee/zomatogeo.csv?raw=true"

st.title('Pune Hotel Recommendation Engine')


lattitude = st.number_input('What Is Your Lattitude')
longitude = st.number_input('What Is Your Longitude')
st.write('Your Geo Location Is ',lattitude,longitude)

def topt(lattitude,longitude):
    df = pd.read_csv(url,index_col=0)
    inlattitude = lattitude * 3.1415/180
    inlongitude = longitude * 3.1415/180
    df["e_distance"] = np.sqrt(((inlattitude - df["rad_latit"] )**2) + ((inlongitude - df["rad_longi"])**2))
    df2 = {'Restaurant_Name': 'My Current Location', 'longitude': longitude, 'lattitude':lattitude, 'e_distance':0  }
    df1 = df.append(df2, ignore_index = True)
    final_data = df1.sort_values(["e_distance"],ascending=True).head(20)
    final_data. rename(columns = {'longitude':'lon', 'lattitude':'lat'}, inplace = True)
    return final_data 
top_20 = topt(lattitude,longitude)
st.write(top_20)
st.map(data=top_20, zoom=None, use_container_width=True)
=======
import streamlit as st
import pandas as pd
import numpy as np
url = "https://github.com/Ck991234/foxy/blob/0a27593660add05b10b01230863c07e591328aee/zomatogeo.csv?raw=true"

st.title('Pune Hotel Recommendation Engine')
dataframe = pd.read_csv(url,index_col=0)
dataframe.rename(columns = {'longitude':'lon', 'lattitude':'lat'}, inplace = True)
st.map(data=dataframe, zoom=None, use_container_width=True)

lattitude = st.number_input('What Is Your Lattitude')
longitude = st.number_input('What Is Your Longitude')
st.write('Your Geo Location Is ',lattitude,longitude)

def topt(lattitude,longitude):
    df = pd.read_csv(url,index_col=0)
    inlattitude = lattitude * 3.1415/180
    inlongitude = longitude * 3.1415/180
    df["e_distance"] = np.sqrt(((inlattitude - df["rad_latit"] )**2) + ((inlongitude - df["rad_longi"])**2))
    df2 = {'Restaurant_Name': 'My Current Location', 'longitude': longitude, 'lattitude':lattitude, 'e_distance':0  }
    df1 = df.append(df2, ignore_index = True)
    final_data = df1.sort_values(["e_distance"],ascending=True).head(20)
    final_data. rename(columns = {'longitude':'lon', 'lattitude':'lat'}, inplace = True)
    return final_data 
top_20 = topt(lattitude,longitude)
st.write(top_20)
st.map(data=top_20, zoom=None, use_container_width=True)
>>>>>>> 0efca08fcd0bc20ecf65d535703f0e2fce6058b5
