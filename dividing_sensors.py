import os
import glob
import pandas as pd
os.chdir(".\clusters\clusters_folder")
rootdir = '.\clusters\clusters_folder'
import numpy as np
colnames= ['ozone','particullate_matter','carbon_monoxide','sulfure_dioxide','nitrogen_dioxide','longitude','latitude','timestamp','cluster_label']
filenames = os.listdir(".")  # get all files' and folders' names in the current directory
result = []
for filename in filenames:  # loop through all the files and folders
    if os.path.isdir(
            os.path.join(os.path.abspath("."), filename)):  # check whether the current object is a folder or not
        result.append(filename)
for r in result:
    path = "./" + str(r)
    extension = 'csv'
    os.chdir(path)
    all_filenames = [c for c in glob.glob('*.{}'.format(extension))]
    counter = 0
    for f in all_filenames:
        df = pd.read_csv(f, names=colnames, low_memory=False)
        df = df[1:]
        if((len(df)/17568).is_integer()):
            list = np.split(df, len(df)/17568)
        elif(len(df)<17568):
            list =[df]
        else:
            raise Exception("Unexpected error in dataset")
        if not os.path.exists("./divided_sensors"):
            os.makedirs("./divided_sensors")
        for l in list:
            path_l= "./divided_sensors/" + str(counter) +".csv"
            counter = counter + 1
            l.index = np.arange(1, len(l)+1)
            l.to_csv(path_l, index=True, header=True)

    os.chdir('../')



