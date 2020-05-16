import pandas as pd
colnames= ['ozone','particullate_matter','carbon_monoxide','sulfure_dioxide','nitrogen_dioxide','longitude','latitude','timestamp','cluster_label']
df = pd.read_csv('./clustered_data.csv', names = colnames, low_memory= False)
df.sort_values(by=['cluster_label'])
# df.to_csv('sorted_clustered_data.csv', index=None, header = True)
