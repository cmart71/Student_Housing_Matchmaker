import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

geocoded_colleges_df = pd.read_csv('chicago_colleges_geoceded.csv')

# # 41.873779 -87.651001 - UIC
geocoded_colleges_df1 = geocoded_colleges_df[['Name','Latitude','Longitude']].copy()
# geocoded_colleges_df1['distance'] = np.sqrt((abs(geocoded_colleges_df1['Latitude'] - 41.873779) ** 2 )+ 
#                                           (abs(geocoded_colleges_df1['Longitude'] - -87.651001) ** 2))

calculateAndInsertDistance(geocoded_colleges_df1, university)
# geocoded_colleges_df1
# subset = geocoded_colleges_df.iloc[10:62]

# print(subset)
# (University of Illinois Chicago) exists in universities

ax = sns.scatterplot(x='Name', y='distance', data=geocoded_colleges_df1)
ax.set_xticks([])
ax.set_xlabel("Universities")