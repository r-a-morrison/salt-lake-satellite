from pathlib import Path
import tarfile
import pandas as pd
import yaml

# Project parameters
config = yaml.safe_load(open('../../project_config.yml'))
input_dir = '../../03_raw_data/Landsat/'
extract_dir = '../../04_processed_data/01_landsat_extracted/'
landsat_summary_file = config['landsat']['summary_file']

scenes_df = pd.read_csv(f'landsat_summary_file')

# Extract files from tar archive
Path(extract_dir).mkdir(parents=False, exist_ok=True)

for scene in scenes_df['display_id']:
    tar = tarfile.open(f'{input_dir}/{scene}.tar')
    tar.extractall(f'{extract_dir}/{scene}')
    tar.close()