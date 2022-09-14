import gspread
from os.path import join, dirname,realpath
from oauth2client.service_account import ServiceAccountCredentials
import argparse
import socket
from config import google_credential_file,USERID

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(join(dirname(realpath(__file__)),google_credential_file), scope)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("--scp",action="store_true", help="Print url and port to be used for scp")

    args = parser.parse_args()

    client = gspread.authorize(creds)
    sheet = client.open("ngrok1p").sheet1

    ip=sheet.acell('B1').value
    port=sheet.acell('C1').value
    if args.scp:
        print("-P {} {}@{}".format(port, USERID, ip))
    else:
        print("{}@{} -p {}".format(USERID,ip, port))

