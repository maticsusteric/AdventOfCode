import os
import requests

from constants import INPUT_BASE_PATH, USER_AGENT
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
SESSION = os.environ.get('SESSION_ID')

def getDailyInputByFolderName():
    # Get basename of current -> ('day' folder)
    day_folder_name = os.path.basename(os.getcwd())
    # Strip (we only need number of day)
    day_num = day_folder_name.lstrip('day')

    # Get the parent folders base name -> ('year' folder)
    year_folder_name = os.path.basename(os.path.dirname(os.getcwd()))
    # Create input url from base path + year + numDay
    input_url = INPUT_BASE_PATH + year_folder_name + '/day/' + day_num + '/input'

    headers = {'User-Agent': USER_AGENT}
    cookies = {'session': SESSION}
    response = requests.get(input_url, headers=headers, cookies=cookies)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        result = response.text.split('\n')
        # Get rid of excess empty string
        result.pop()
        return result
    else:
        # Handle unsuccessful request
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None
