import os
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

##### FILL WITH YOUR DATAS
path="<PATH TO TCX DIR>"   # the directory must contain only tcx files and no subdirs
client_id="<YOUR CLIENT ID>"
client_secret="<YOUR CLIENT SECRET KEY>"
refresh_token="<YOUR REFRESH TOKEN WITH ACTIVITY WRITE PERMISSION>"
########

auth_url = "https://www.strava.com/oauth/token"
activities_url = "https://www.strava.com/api/v3/uploads"
test_url = "https://www.strava.com/api/v3/athlete"

payload = {
    'client_id': client_id,
    'client_secret': client_secret,
    'refresh_token': refresh_token,
    'grant_type': "refresh_token",
    'f': 'json'
}




res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']


arr = os.listdir(path)
print(len(arr))

for x in arr:
    payloadact = {
        'name': x,
        'description': 'Traccia caricata da Endomondo attraverso script',
        'trainer': '0',
        'commute': '0',
        'data_type': 'tcx',
        'external_id': client_id
    }
    files = {'file': open(path+x, 'rb')}
    print(path+x)
    header = {'Authorization': 'Bearer ' + access_token}
    risultato = requests.post(activities_url, files=files, data=payloadact, headers=header).text
    print(risultato)

