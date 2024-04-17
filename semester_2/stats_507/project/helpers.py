## data download and cleaning functions
import requests
import zipfile
import os

def download_and_zip(url, zip_path, overwrite=False):
    try:
        # Check if the file exists and if overwrite is False, 
        # skip downloading and zipping
        if os.path.exists(zip_path):
            if not overwrite:
                print("The file already exists and will not be overwritten.")
                return
            else:
                os.remove(zip_path)
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            temp_file = 'temp_file'
            with open(temp_file, 'wb') as f:
                f.write(response.content)

            with zipfile.ZipFile(zip_path, 'w') as zipf:
                zipf.write(temp_file, os.path.basename(url))

            os.remove(temp_file)
            print("File downloaded and zipped successfully!")
        else:
            print(f"Failed to download the file: HTTP Status Code {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

## testing
# file_url = 'https://data.cdc.gov/api/views/hksd-2xuw/rows.csv?accessType=DOWNLOAD'
# zip_path = 'cdc_data.zip'
# # # Download the file and zip it
# download_and_zip(file_url, zip_path)
# download_and_zip(file_url, zip_path, overwrite=False)

