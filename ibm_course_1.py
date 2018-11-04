import pandas as panda 

from matplotlib import pyplot as plot 
import folium


json_file = 'C:\\Users\\somak\\Documents\\somak_python\\matplotlib_learning\\san-francisco.geojson'



remote_location = 'https://cocl.us/sanfran_crime_dataset'
data = panda.read_csv(remote_location)

data_frame = data[['Category','PdDistrict']].groupby('PdDistrict', axis=0).count()
data_frame.reset_index()
data_frame['Neighborhood'] = data_frame.index
# data_frame.columns = ['Neighborhood', 'Count']
data_frame.index = list(range(0, data_frame.shape[0]))
data_frame = data_frame[['Neighborhood', 'Category']]

data_frame.columns = ['Neighborhood', 'Count']




print(data_frame)

import numpy as np
# create a numpy array of length 6 and has linear spacing from the minium total immigration to the maximum total immigration
threshold_scale = np.linspace(data_frame['Count'].min(),
                              data_frame['Count'].max(),
                              6, dtype=int)
threshold_scale = threshold_scale.tolist() # change the numpy array to a list
threshold_scale[-1] = threshold_scale[-1] + 1 # make sure that the last value of the list is greater than the maximum immigration



# create a plain world map
world_map = folium.Map(location=[37.77, -122.42], zoom_start=12)

# generate choropleth map using the total immigration of each country to Canada from 1980 to 2013
world_map.choropleth(
    geo_data=json_file,
    data=data_frame,
    columns=['Neighborhood', 'Count'],
    key_on='feature.properties.DISTRICT',
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,

    threshold_scale=threshold_scale,
    legend_name='Crime Rate In Sanfrancisco',
    reset = True
)
world_map.save("C:\\Users\\somak\\Documents\\somak_python\\matplotlib_learning\\somak.html")
world_map


