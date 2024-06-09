import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# A Google által támogatott OAuth 2.0 hitelesítési áramlatainak elérhetősége
flow = InstalledAppFlow.from_client_secrets_file(
    'credentials.json',
    scopes=['https://www.googleapis.com/auth/calendar.readonly']
)

# Folyamat elindítása a felhasználó hitelesítéséhez
credentials = flow.run_local_server(port=0)

# A hitelesítő adatok mentése
with open('token.json', 'w') as token:
    token.write(credentials.to_json())

print("Hitelesítő adatok mentve.")
