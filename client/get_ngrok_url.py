import gspread
from os.path import join, dirname,realpath
from oauth2client.service_account import ServiceAccountCredentials
fromo config import google_credential_file
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(join(dirname(realpath(__file__)),google_credential_file), scope)
client = gspread.authorize(creds)
sheet = client.open("Rpi Ngrok URL").sheet1

url=sheet.acell('A1').value
#print(url)
new_url, port = url.split("//")[1].split(":")
print("pi@{} -p {}".format(new_url, port))

