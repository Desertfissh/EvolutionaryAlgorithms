import pandas as pd
df = pd.read_csv('gb_cities.csv')

names = df['Place Name'].values
coordinates = df[['Longitude', 'Latitude']].values

import routingpy as rp
import numpy as np

api_key = 'e52ccff1-291d-421a-870d-25aa97333e75'
api = rp.Graphhopper(api_key=api_key)
matrix = api.matrix(locations=coordinates, profile='car')
durations = np.matrix(matrix.durations)
np.savetxt('./CaliforniaDurationMatrix.csv', durations, delimiter=',')