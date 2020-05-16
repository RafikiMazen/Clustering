import os
import glob
import pandas as pd
os.chdir(".\clusters")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
colnames= ['ozone','particullate_matter','carbon_monoxide','sulfure_dioxide','nitrogen_dioxide','longitude','latitude','timestamp','cluster_label']
for f in all_filenames:
    df = pd.read_csv(f, names=colnames,low_memory=False)
    l = [x for _, x in df.groupby(['longitude','latitude'])]
    counter = 0
    for i in l:
        if not os.path.exists("./clusters_folder/" + str(f[0])):
            os.makedirs("./clusters_folder/" + str(f[0]))
        path = "./clusters_folder/" + str(f[0]) +"/" + str(counter)+'.csv'
        counter = counter + 1
        i.to_csv(path, index=None, header=True)