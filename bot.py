"""
file for bot creation

"""
import os
from datetime import datetime
from pathlib import Path
from flask import Flask
from slackeventsapi import SlackEventAdapter
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

CHANNELS = ['reactjs','java','sql','powerbi', 'projects','random', 'support','data','frontend','backend', 'javascript','python','html-css','nodejs']

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
client = WebClient(token=os.environ.get('SLACK_TOKEN'))
app = Flask(__name__)

slack_event_adapter = SlackEventAdapter(os.environ.get('SIGNING_SECRET'), 'slack/events', app)

@slack_event_adapter.message.on('message')

# sending messages
def send_message_to_channels(message, channels):
    for channel in channels:
        print(channel)
        try:
            client.chat_postMessage(channel='#{}'.format(channel), text=message)
        except SlackApiError as e:
            print(f"Error: {e}")


#  handling events
if __name__ == "__main__":
    app.run(debug=True)