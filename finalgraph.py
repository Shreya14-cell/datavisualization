import plotly.express as px
import pandas as pd

# Load your datasets
landslide_data = pd.read_csv('cleaned-landslide-data.csv')
population_density = pd.read_csv('Population_density.csv')

# Prepare the data (select population density for 2016 and merge with landslide data)
population_density_2016 = population_density[['country', '2016']].copy()  # Ensure you create a copy
population_density_2016.columns = ['country_name', 'population_density_2016']  # Rename columns directly
merged_data = pd.merge(landslide_data, population_density_2016, how='left', on='country_name')

# Create an interactive global map
fig = px.scatter_geo(merged_data,
                     lat='latitude',
                     lon='longitude',
                     color='landslide_category',
                     hover_name='event_title',
                     hover_data=['country_name', 'population_density_2016', 'event_date'],
                     title='Global Map of Landslide Events with Population Density (2016)',
                     projection='natural earth')

# Show the map
fig.show()
