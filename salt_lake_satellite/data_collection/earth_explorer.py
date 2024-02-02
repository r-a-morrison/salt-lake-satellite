from pathlib import Path
import yaml
import pandas as pd
from landsatxplore.api import API
from landsatxplore.earthexplorer import EarthExplorer

def get_usgs_cred():
    """Handles username and password for USGS API. Credentials for EarthExplorer can be obtained at https://earthexplorer.usgs.gov"""

    with open(Path.home() / '.usgs.yml', 'r') as stream:
        try:
            cred = yaml.safe_load(stream)['usgs']
            usgs_user = cred['username']
            usgs_pw = cred['password']
            return usgs_user, usgs_pw
        except yaml.YAMLError as exc:
            print(exc)

def initialize_usgs_api():
    """Initializes USGS EarthExplorer API call to search Landsat database"""

    usgs_user, usgs_pw = get_usgs_cred()
    return API(usgs_user, usgs_pw)

def initialize_usgs_earthexplorer():
    """Initializes USGS EarthExplorer API call to download Landsat database"""

    usgs_user, usgs_pw = get_usgs_cred()
    return EarthExplorer(usgs_user, usgs_pw)

def get_search_info(scenes):
    """Takes USGS EarthExplorer API search results and parses results into a dataframe"""

    scenes_df = pd.DataFrame(scenes)
    scenes_df = scenes_df[[
        'entity_id', 'display_id', 'wrs_path', 
        'wrs_row', 'satellite', 'cloud_cover', 
        'acquisition_date', 'start_time', 'stop_time', 
        'day-night_indicator'
    ]]
    scenes_df.sort_values('acquisition_date', ascending=False, inplace=True)
    return scenes

def download_data(display_ids, path_dir):
    """Given a set of USGS EarthExplorer display ids, calls EarthExplorer and downloads tar files of satellite imagery to the specified directory"""

    print('INFO: Error "Download failed with dataset id 1 of 2" can be safely ignored. This is a bug with the landsatexplore package.')
    ee = initialize_usgs_earthexplorer()

    Path(path_dir).mkdir(parents=False, exist_ok=True)

    for display_id in display_ids:
        if not Path(f'{path_dir}/{display_id}.tar').is_file():
            try: 
                ee.download(display_id, output_dir=path_dir)
                print(f'SUCCESS: {display_id} downloaded')
            # FYI: The packages raises an additional error, even when download is successful
            except:
                print(f'ERROR: Problem downloading {display_id}')
        else:
            print(f'{display_id} already exists')

    ee.logout()