# ngrok_url
NGROK provides a public endpoint to allow a client to connect to a server with no public-facing IP address. If you are on a free subscription, this endpoint will change when you restart the service. This little hack automates the server such that it updates the new endpoint URL on a Google spreadsheet, and the client-side can use the URL obtained from the spreadsheet to connect to the server.

## Requirements

### Client
oauth2client
gspread

### Server
oauth2client
gspread
pyngrok


## Installation
1. Login to NGROK dashboard and get you Authtoken. 
2. Enable Google API. Follow the instruction at https://medium.com/@CROSP/manage-google-spreadsheets-with-python-and-gspread-6530cc9f15d1 and get a key file in JSON format. 

3. Update your config.py

4. Fix ngrok.service to point to the correct Python interpreter and location of ngrok_service.py
```
sudo systemctl enable ngrok
sudo systemctl start ngrok
```
