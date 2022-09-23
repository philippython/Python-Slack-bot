"""
file for bot creation

"""
import os
import slack
from pathlib import Path
from dotenv import load_dotenv
import time

CHANNELS_1 =  ['projects','random', 'support','data','frontend']
CHANNELS_2 =  ['announcements','backend', 'javascript']
CHANNELS_3 =  ['python','html-css','nodejs']
CHANNELS_4 =  ['reactjs','java','sql','powerbi']
CHANNELS = ['reactjs','java','sql','powerbi', 'projects','random', 'support','data','frontend','announcements','backend', 'javascript','python','html-css','nodejs']

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ.get('SLACK_TOKEN'))

for channel in CHANNELS:
    time.sleep(2)
    print(channel)
    client.chat_postMessage(channel='#{}'.format(channel), text="""
                            Hello everyone I'm a Bot built by Odulaja philip to detect rules violators and assessments defaulters my name is SHEGE...I'm a nice bot, I hope we get along, Nice to meet you all""")