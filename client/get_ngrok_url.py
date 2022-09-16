import argparse
import requests,json
from config import USERID,GLITCH_URL

if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("--scp",action="store_true", help="Print url and port to be used for scp")

    args = parser.parse_args()

    response=requests.get(f"{GLITCH_URL}/messages")
    #reponse eg: {"chat":[{"id":1,"message":"4.tcp.ngrok.io|3.131.147.49|17526|2022-09-06 13:44:43"}]}
    message=json.loads(response.content.decode('utf-8'))['chat'][0]['message'].split('|')

    _,ip,port,_=message

    if args.scp:
        print("-P {} {}@{}".format(port, USERID, ip))
    else:
        print("{}@{} -p {}".format(USERID,ip, port))

