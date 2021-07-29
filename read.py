from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account


SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1pB89_1HdbZ4mUMf_9kr-m36jaWolhxAgQf0anO2e_ig'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Comments!A1:F318").execute()
values = result.get('values', [])
request = sheet.values().update(
    spreadsheetID=SAMPLE_SPREADSHEET_ID, range="Comments!A1:F318", valueInputOption="User_Entered", body=value_range_body).execute
print(values)
