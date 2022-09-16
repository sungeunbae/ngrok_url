# ngrok_url
NGROK provides a public endpoint to allow a client to connect to a server with no public-facing IP address. If you are on a free subscription, this endpoint will change when you restart the service. This little hack automates the server such that it updates the new endpoint URL on Glitch-hosted SQLite, and the client-side can use the URL obtained from the SQLite.

## Requirements


### Server
pyngrok


## Installation
1. Login to NGROK dashboard and get you Authtoken. 
2. Go to Glitch, start a new project based on glitch-hello-sqlite. Just need to update admin_key in .env
3. Update your config.py 

4. Fix ngrok.service to point to the correct Python interpreter and location of ngrok_service.py
```
sudo systemctl enable ngrok
sudo systemctl start ngrok
```

