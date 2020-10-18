import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


class WriteToSpreadSheet:
    def __init__(self, data):
        self.data = data

    def write_data(self):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('PythonContactMe-353333927756.json', scope)

        client = gspread.authorize(creds)

        df = pd.DataFrame.from_dict(data)

        sheet = client.open('contact_me_page')
        sheet.add_worksheet(rows=20, cols=2, title='random')
        sheet_persons = sheet.get_worksheet(1)
        sheet_persons.insert_rows(df)
        print(sheet_persons)


if __name__ == '__main__':
    data = {'email': 'test', 'from': 'test', 'message': 'test'}
    csv = WriteToSpreadSheet(data)
    csv.write_data()
