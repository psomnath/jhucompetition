# pip install google-api-python-client
# Checkout the instruction in this youtube video - https://www.youtube.com/watch?v=tamT_iGoZDQ
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload,MediaIoBaseDownload
from google.oauth2 import service_account
import datetime
import io
import pandas as pd
config = {'creds' : service_account.Credentials.from_service_account_file('jhucompetition-7b33c809fa56.json', scopes=['https://www.googleapis.com/auth/drive'])
          , 'folder_id' : '1oAPXQdITafmrwX8DasVYhBE9YEBgHl4s'
          , 'mime_type' : {'csv' : 'text/plain', 'txt' : 'text/plain', 'pkl' : 'application/octet-stream', 'py' : 'text/plain', 'json' : 'application/json'\
              ,'xlsx' : 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'}}

def write_file(file_name,user_id = '',duplicate_allowed=False,config=config):
    file_extension = file_name.split('.')[-1]
    file_first_name = file_name.replace(file_extension,'')[:-1]
    file_name_contains = [file_first_name,file_extension]
    mime_type = config['mime_type'][file_extension] if (file_extension in config['mime_type'])  else ''
    if mime_type == '':
        error = 'Unsupported file : '+file_name
        return(False,'',error)
    else:
        if duplicate_allowed:
            dt = datetime.datetime.now()
            postfix = ''
            if user_id != '':
                postfix = user_id+'.'
            postfix += str(dt.year)+'.'+str('%02d' % dt.month)+'.'+str('%02d' % dt.day)+'.'+str('%02d' % dt.hour)+'.'+str('%02d' % dt.minute)+'.'+str('%02d' % dt.second)
            write_file_name = file_first_name + '.' + postfix + '.' + file_extension
        else:
            write_file_name = file_name
        service = build('drive', 'v3', credentials=config['creds'])
        file_metadata = {'name' : write_file_name,'parents' : [config['folder_id']]}
        try:
            file = service.files().create(
                body=file_metadata,
                media_body = MediaFileUpload(file_name, mimetype=config['mime_type'][file_extension])
            ).execute()
            return(True,file.get('name'),'')
        except Exception as e:
            return(False,'',e)

def read_files(file_name,user_id = '',config=config):
    file_extension = file_name.split('.')[-1]
    file_first_name = file_name.replace(file_extension,'')[:-1]
    file_name_contains = [file_first_name,file_extension]
    if user_id != '':
        file_name_contains.append(user_id)
    mime_type = config['mime_type'][file_extension] if (file_extension in config['mime_type'])  else ''
    fetched_file_list = []
    if mime_type == '':
        print('Unsupported file : ',file_name)
    else:
        service = build('drive', 'v3', credentials=config['creds'])
        query = f"'{config['folder_id']}' in parents"
        results = service.files().list(q=query, fields="nextPageToken, files(id, name)").execute()
        fetched_files = results.get('files', [])

        for fetched_file in fetched_files:
            fetched_file_name = fetched_file['name']
            fetched_file_extension = fetched_file_name.split('.')[-1]
            

            if len(file_name_contains) == len([1 for x in file_name_contains if x in fetched_file_name]):
                
                fetched_file_id = fetched_file['id']
                file_metadata = service.files().get(fileId=fetched_file_id, fields='name, mimeType').execute()
                fetched_file_mime_type = file_metadata.get('mimeType')
                if  mime_type ==  fetched_file_mime_type:         
                    request = service.files().get_media(fileId=fetched_file_id)
                    fetched_file_content = io.BytesIO()
                    downloader = MediaIoBaseDownload(fetched_file_content, request)
                    done = False
                    while done is False:
                        status, done = downloader.next_chunk()
                    fetched_file_content.seek(0)
                    if fetched_file_mime_type == 'text/plain':
                        fetched_file_content = fetched_file_content.getvalue().decode('utf-8')
                    if fetched_file_extension == 'csv':
                        fetched_file_content = io.StringIO(fetched_file_content) 
                    fetched_file_list.append({'file_name' : fetched_file_name, 'file_id' : fetched_file_id, 'file_content': fetched_file_content\
                        , 'mime_type' : fetched_file_mime_type,'file_extension':fetched_file_extension})
                    
    return(fetched_file_list)

'''#status, file_name,error = write_file('accounts.csv',user_id = '',duplicate_allowed=False, config=config)
status, file_name,error = write_file('accounts.csv')
print(status, file_name,error)
#status, file_name,error = write_file('Customers.csv',user_id = '',duplicate_allowed=True, config=config)
status, file_name,error = write_file('Customers.csv',duplicate_allowed=True)
print(status, file_name,error)
#status, file_name,error = write_file('random_model.pkl',user_id = 'spurkay1',duplicate_allowed=True, config=config)
status, file_name,error = write_file('random_model.pkl',user_id = 'spurkay1',duplicate_allowed=True)
print(status, file_name,error)'''

'''#fetched_files = read_files('accounts.csv',user_id = '',config=config)
fetched_file_list = read_files('accounts.csv')
for fetched_file in fetched_file_list:
    df = pd.read_csv(fetched_file['file_content'])
    print(df.head(1))'''
    
'''#fetched_file_list = read_files('Customers.csv',user_id = '',config=config)
fetched_file_list = read_files('Customers.csv',config=config)
for fetched_file in fetched_file_list:
    df = pd.read_csv(fetched_file['file_content'])
    print(df.head(1))'''

#fetched_file_list = read_files('random_model.pkl',user_id = 'spurkay1',config=config)
fetched_file_list = read_files('random_model.pkl',user_id = 'spurkay1')
for fetched_file in fetched_file_list:
    print(fetched_file)
