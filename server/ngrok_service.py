from pyngrok import ngrok
import os

from datetime import datetime
import requests,json
import socket

from config import GLITCH_URL,GLITCH_KEY,ngrok_token

url_file="/tmp/ngrok.url"

header={'admin_key':GLITCH_KEY}

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
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data={'id':"1",'message':f"{new_url}|{ip}|{port}|{timestamp}"}
    response=requests.put(f"{GLITCH_URL}/message", data=data, headers=header)
    success=json.loads(response.content.decode('utf-8'))['success']


if success:
    print("Successfuly created a tunnel")
else:
    print("Something went wrong")
ngrok_process =ngrok.get_ngrok_process()
try:
    ngrok_process.proc.wait()
except KeyboardInterrupt:
    print("Shutting down server")
    ngrok.kill()


