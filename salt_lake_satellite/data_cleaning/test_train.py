import re
from datetime import datetime
from pathlib import Path
import shutil

def get_new_display_id(row):
    test_date = datetime.strptime(row['start_time'], '%Y-%m-%d %H:%M:%S.%f')
    new_date = test_date.strftime('%Y%m%d%H%M%S')
    start_id = re.findall(r'(LC\d{2}_L1TP_\d{6}_)\d{8}_\d{08}_\d{02}_T1', row['display_id'])[0]
    end_id = re.findall(r'LC\d{2}_L1TP_\d{6}_\d{8}(_\d{08}_\d{02}_T1)', row['display_id'])[0]
    new_id = f'{start_id}{new_date}{end_id}'
    return new_id

def copy_scene(source, destination):
    file_name = Path(destination).stem
    try:
        shutil.copy(source, destination)
    except shutil.SameFileError:
        print(f'{file_name}: Source and destination represents the same file.')
    except PermissionError:
        print(f'{file_name}: Permission denied.')
    except:
        print(f'{file_name}: Error occurred while copying file.')

def write_dfs_with_new_display_id(df, source_dir, output_dir, bands):
    for scene in df['display_id']:
        for band in bands:
            new_display_id = df[df['display_id'] == scene]['new_display_id'].item()
            source_path = f'{source_dir}{scene}/{scene}_{band}.TIF'
            output_subdir = f'{output_dir}{new_display_id}/'
            output_path = f'{output_subdir}/{new_display_id}_{band}.TIF'

            Path(output_subdir).mkdir(parents=True, exist_ok=True)
            copy_scene(source_path, output_path)

