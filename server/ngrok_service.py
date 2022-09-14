from pyngrok import ngrok
import time
import os

import gspread
from os.path import join, dirname,realpath
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from config import google_credential_file,ngrok_token
import socket

url_file="/tmp/ngrok.url"
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(join(dirname(realpath(__file__)),google_credential_file), scope)
client = gspread.authorize(creds)
sheet = client.open("ngrok1p").sheet1


ngrok.set_auth_token(ngrok_token)

if os.path.exists(url_file):
    os.remove(url_file)
with open(url_file,"w") as f:
    ssh_tunnel = ngrok.connect(22, "tcp")
    url=ssh_tunnel.public_url
    new_url,port = url.split("//")[1].split(":")
    ip=socket.gethostbyname(new_url)
    print(url)
    print(ip)
    f.write(url+"\n")
    sheet.update("A1",new_url)
    sheet.update("B1",ip)
    sheet.update("C1",port)
    sheet.update("D1",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print("Successfuly created a tunnel")    
ngrok_process =ngrok.get_ngrok_process()
try:
    ngrok_process.proc.wait()
except KeyboardInterrupt:
    print("Shutting down server")
    ngrok.kill()


