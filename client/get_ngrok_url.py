import gspread
from os.path import join, dirname,realpath
from oauth2client.service_account import ServiceAccountCredentials
import argparse

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(join(dirname(realpath(__file__)),'vejgarden-4efd839296c1.json'), scope)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("--scp",action="store_true", help="Print url and port to be used for scp")

    args = parser.parse_args()

    client = gspread.authorize(creds)
    sheet = client.open("Rpi Ngrok URL").sheet1

    url=sheet.acell('A1').value
    #print(url)
    new_url, port = url.split("//")[1].split(":")
    if args.scp:
        print("-P {} pi@{}".format(port, new_url))
    else:
        print("pi@{} -p {}".format(new_url, port))

