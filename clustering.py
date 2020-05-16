import pandas as pd
import descartes
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
from shapely.geometry import Point,Polygon
from sklearn.cluster import KMeans



colnames= ['ozone','particullate_matter','carbon_monoxide','sulfure_dioxide','nitrogen_dioxide','longitude','latitude','timestamp']
df = pd.read_csv('./pollution data/combined_dataset.csv', names = colnames)

# plt.scatter(x=df['longitude'], y=df['latitude'])
# plt.show()
kmeans = KMeans(n_clusters=4)
kmeans.fit(df[['longitude','latitude']])
y_kmeans = kmeans.predict(df[['longitude','latitude']])
plt.scatter(df['longitude'],y=df['latitude'], c=y_kmeans, s=50, cmap='viridis')
df['cluster_label']=y_kmeans

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()
# df.to_csv ('clustered_data.csv', index=None, header = True)