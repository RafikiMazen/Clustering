import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans



colnames= ['ozone','particullate_matter','carbon_monoxide','sulfure_dioxide','nitrogen_dioxide','longitude','latitude','timestamp']
df = pd.read_csv('./pollution data/combined_dataset.csv', names = colnames)
K_clusters = range(1,10)
kmeans = [KMeans(n_clusters=i) for i in K_clusters]
Y_axis = df[['latitude']]
X_axis = df[['longitude']]
score = [kmeans[i].fit(Y_axis).score(Y_axis) for i in range(len(kmeans))]# Visualize
plt.plot(K_clusters, score)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')
plt.show()
