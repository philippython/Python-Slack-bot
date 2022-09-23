"""
file for bot creation

"""
import os
from pathlib import Path
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

CHANNELS = ['reactjs','java','sql','powerbi', 'projects','random', 'support','data','frontend','announcements','backend', 'javascript','python','html-css','nodejs']

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = WebClient(token=os.environ.get('SLACK_TOKEN'))

for channel in CHANNELS:
    print(channel)
    try:
        client.chat_postMessage(channel='#{}'.format(channel), text=
"""
To Join your respective groups, click the group tag below, only join a group at a time, for example if you are a Frontend dev and you have already mastered html and css but not JavaScript then join the JavaScript group:

HTML & CSS: #html-css
JavaScript: #javascript
NodeJs: #nodejs
React: #reactjs
Python: #python
Java: #java
SpringBoot: #springboot
UX/UI: #product-design
Data Analyst (Power BI): #data
Data/SQL: #sql
""")
    except SlackApiError as e:
        print(f"Error: {e}")
