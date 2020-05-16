import pandas as pd
import glob
colnames= ['ozone','particullate_matter','carbon_monoxide','sulfure_dioxide','nitrogen_dioxide','longitude','latitude','timestamp','cluster_label']
g = pd.read_csv('./sorted_clustered_data.csv', names = colnames, low_memory= False).groupby('cluster_label')
g.apply(lambda x: x.to_csv(r'.\clusters\{}.csv'.format(x.name)))
# glob.glob(r'.\cluster*.csv')
