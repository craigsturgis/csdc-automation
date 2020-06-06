import requests
import os

airtable_api_key = os.environ.get("AIRTABLE_API_KEY")

headers = {"Authorization": "Bearer {0}".format(airtable_api_key)}

r = requests.get("https://api.airtable.com/v0/appykcYvsvUKNzFBh/Contacts", headers=headers)

print(r.json())