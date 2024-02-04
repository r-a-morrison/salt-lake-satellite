import pandas as pd
import yaml
from sklearn.model_selection import train_test_split
from salt_lake_satellite.data_cleaning import test_train

config = yaml.safe_load(open('project_config.yml'))
landsat_summary_file = config['landsat']['summary_file']
landsat_bands = config['landsat']['bands']
landsat_extracted_path = '04_processed_data/01_landsat_extracted/'
train_path = '04_processed_data/02_landsat_train/'
test_path = '04_processed_data/03_landsat_test/'

landsat_df = pd.read_csv(landsat_summary_file)

'''
FYI: LandsatXplore automatically downloads both Systematic Terrain
Correction (L1GT) and Terrain Precision Correction (L1TP) scenes,
but only L1TP scenes seem to have useable data for this time and region.
'''
landsat_l1tp_df = landsat_df[landsat_df['display_id'].str.contains('L1TP')]

'''
FYI: TorchGeo Landsat class assumes a date stamp in .TIF file name. This date
stamp is used to define the bounding box in time. Later, TorchGeo will use the 
bounding box to determine which truth mask corresponds with which scene.
Because we have multiple images in the same area on the same day, we need a 
bounding box that is more precise than one day. get_new_display_id() replaces 
the date stamp in the file name with a datetime stamp. Without a datetime stamp,
the truth mask files cannot be properly assigned to their corresponding scene.
'''
new_display_id = landsat_l1tp_df.apply(test_train.get_new_display_id, axis=1)
landsat_l1tp_df = landsat_l1tp_df.assign(new_display_id=new_display_id.values)

train_df, test_df = train_test_split(landsat_l1tp_df,
                                     test_size=0.33,
                                     stratify=landsat_l1tp_df[['day-night_indicator']])

train_df.to_csv('04_processed_data/landsat_train.csv', index=False)
test_df.to_csv('04_processed_data/landsat_test.csv', index=False)

test_train.write_dfs_with_new_display_id(train_df,
                                         source_dir=landsat_extracted_path,
                                         output_dir=train_path,
                                         bands=landsat_bands)
test_train.write_dfs_with_new_display_id(test_df, 
                                         source_dir=landsat_extracted_path, 
                                         output_dir=test_path,
                                         bands=landsat_bands)