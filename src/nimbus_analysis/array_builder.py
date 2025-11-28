import numpy as np
from urllib.request import urlopen



def get_nimbus_data(target_date):
    """query NASA archive to get the satellite data for a given date

    Args:
        target_date (str): date of interest in format YYYYmmdd
    """
    
    value_list = []
    target_url = f'https://ozonewatch.gsfc.nasa.gov/data/nimbus7/Y{target_date[:4]}/L3_ozone_n7t_{target_date}.txt'

    try:
        for line in urlopen(target_url):
            value_list.append(line)
    except:
        print(f'no data for {target_date}')

    value_list = value_list[3:]
    
    return value_list



def str_to_array(value_list):
    """
    convert the downloaded string to an array of integers
    """
    value_array = []
    lat_entry = []

    for i in range(len(value_list)):
        
        if (i+1)%12==0:
            lat_entry_partial = value_list[i][1:40]
            lat_entry_partial = [lat_entry_partial[j:j+3] for j in range(0, len(lat_entry_partial), 3)]
            lat_entry = lat_entry + lat_entry_partial
            value_array.insert(0,lat_entry)
            lat_entry = []
            
        else:
            lat_entry_partial= value_list[i][1:-1]
            lat_entry_partial = [lat_entry_partial[j:j+3] for j in range(0, len(lat_entry_partial), 3)]
            lat_entry = lat_entry + lat_entry_partial
            
    value_array = np.array(value_array).astype(int)
    return value_array