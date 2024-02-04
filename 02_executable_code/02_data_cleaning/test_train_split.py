import pandas as pd
import yaml
from sklearn.model_selection import train_test_split
import numpy as np

config = yaml.safe_load(open('project_config.yml'))
landsat_summary_file = config['landsat']['summary_file']

landsat_df = pd.read_csv(landsat_summary_file)
# FYI: LandsatXplore automatically downloads both Systematic Terrain
# Correction (L1GT) and Terrain Precision Correction (L1TP) scenes,
# but only L1TP scenes seem to have useable data for this time and region.
landsat_l1tp_df = landsat_df[landsat_df['display_id'].str.contains('L1TP')]
train, test = train_test_split(landsat_l1tp_df, 
                          test_size=0.33, 
                          stratify=landsat_df[['day-night_indicator']])

train.to_csv('04_processed_data/landsat_train.csv', index=False)
test.to_csv('04_processed_data/landsat_test.csv', index=False)