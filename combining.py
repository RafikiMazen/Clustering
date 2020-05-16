import pandas as pd
import glob
import os
os.chdir(".\pollution data")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
# combined_csv.to_csv( "combined_dataset.csv", index=False, encoding='utf-8-sig')


