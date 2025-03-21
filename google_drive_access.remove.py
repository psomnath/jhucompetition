# pip install google-api-python-client

# conda install conda-forge::google-api-python-client
# conda install conda-forge::google-auth-oauthlib
# Checkout the instruction in this youtube video - https://www.youtube.com/watch?v=tamT_iGoZDQ

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2 import credentials

# Replace with your credentials and file details
CLIENT_SECRETS_FILE = 'jhucompetition-7b33c809fa56.json'
SCOPES = ['https://www.googleapis.com/auth/drive.file']  # Or a more specific scope
FILE_PATH = ''
FILE_NAME = 'random_model.pkl'
PARENT_FOLDER_ID = '1oAPXQdITafmrwX8DasVYhBE9YEBgHl4s' # Optional: If you want to upload to a specific folder
MIME_TYPE = 'application/octet-stream' #for binary pickle file #'text/plain' -- for normal text file

# Authenticate
flow = InstalledAppFlow.from_client_secrets_file(
    CLIENT_SECRETS_FILE, SCOPES
)
credentials = flow.credentials

# Build the Drive API service
drive_service = build('drive', 'v3', credentials=credentials)

# Prepare the file metadata
file_metadata = {
    'name': FILE_NAME,
    'parents': [PARENT_FOLDER_ID] if PARENT_FOLDER_ID else []  # Optional parent folder
}

# Create the MediaFileUpload object
media = MediaFileUpload(FILE_PATH, mimetype=MIME_TYPE)  # Replace with your file's MIME type

# Upload the file
try:
    file = drive_service.files().create(
        body=file_metadata,
        media=media
    ).execute()
    print(f'File uploaded: {file.get("name")}')
except Exception as e:
    print(f'An error occurred: {e}')