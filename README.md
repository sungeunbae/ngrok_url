# ngrok_url
Requirements

Client
oauth2client
gspread

Server
oauth2client
gspread
pyngrok

Get ngrok authtoken and a key file from Google API (https://medium.com/@CROSP/manage-google-spreadsheets-with-python-and-gspread-6530cc9f15d1) and add them to config.py

Fix ngrok.service to point to the correct Python interpreter and location of ngrok_service.py

sudo systemctl enable ngrok
sudo systemctl start ngrok
