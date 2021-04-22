from pyngrok import ngrok
import time
import os

import gspread
from os.path import join, dirname,realpath
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from config import google_credential_file,ngrok_token

url_file="/tmp/ngrok.url"
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(join(dirname(realpath(__file__)),google_credential_file), scope)
client = gspread.authorize(creds)
sheet = client.open("Rpi Ngrok URL").sheet1


ngrok.set_auth_token(ngrok_token)

if os.path.exists(url_file):
    os.remove(url_file)
with open(url_file,"w") as f:
    ssh_tunnel = ngrok.connect(22, "tcp")
    url=ssh_tunnel.public_url
    print(url)

    f.write(url+"\n")
    sheet.update("A1",url)
    sheet.update("B1",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print("Successfuly created a tunnel")    
ngrok_process =ngrok.get_ngrok_process()
try:
    ngrok_process.proc.wait()
except KeyboardInterrupt:
    print("Shutting down server")
    ngrok.kill()


