from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from twitchAPI.twitch import Twitch
import json
from datetime import *

def get_streamer_id(name: str):
    streamer_data = twitch.get_users(logins=name)['data']
    if streamer_data:
        return int(streamer_data[0]['id'])
    else:
        f = open('streamers.json','r',encoding='utf-8')
        json_data = json.load(f)
        streamer_id = int(json_data['streamer_ids'][name])
        f.close()
        return streamer_id

def get_streamer_schedule(channel_id: int):
    streamer_schedule_data = twitch.get_channel_stream_schedule(broadcaster_id=channel_id)
    streamer_schedule = []
    # if no streams are scheduled
    try:
        streamer_schedule = streamer_schedule_data['data']['segments']
    except:
        return None
    else:
        return streamer_schedule

def format_schedule(schedule: list,streamer: str):
    formattedSchedule = []
    for stream in schedule: # format streams into google calendar events
        if stream['category'] == None: # check if a category is listed
            summary=streamer + ': ' + stream['title']
        else:
            summary=streamer + ': ' + stream['title'] + ' | ' + stream['category']['name']
        start=datetime.fromisoformat(str(stream['start_time']))
        end = ''
        if stream['end_time'] == None: # if no end time, default to 1 hour
            end=start + timedelta(hours=1)
        else:
            end=datetime.fromisoformat(str(stream['end_time']))
        description=stream['id']
        formattedSchedule.append(Event(summary=summary,start=start,end=end,description=description)) # add event to list
    return formattedSchedule # return list of event types



# initalize twitch api
f = open('twitch_secrets.json', 'r')
jsonData = json.load(f)
client_id = jsonData['client_id']
client_secret = jsonData['client_secret']
f.close()
twitch = Twitch(client_id, client_secret)

# initialize google calendar
global calendarID
with open('google_secrets.json','r',encoding='utf-8') as calendar_id:
    calendarID = json.load(calendar_id)['calendar_id']
calendar_id.close()
calendar = GoogleCalendar(default_calendar=calendarID,credentials_path='credentials.json')

# list of streamers
f = open('streamers.json','r',encoding='utf-8')
streamers = json.load(f)['streamers']
f.close()

# make list of streams already in calendar
stream_ids = []
for e in calendar.get_events(date.today(),date.today() + timedelta(days=100)):
    stream_ids.append(e.description)

for streamer in streamers:
    # get streamer schedule
    streamer_id = get_streamer_id(streamer)
    schedule = get_streamer_schedule(streamer_id)
    
    # format segments for calendar
    if schedule: # check if schedule is not empty
        formattedSchedule = format_schedule(schedule,streamer)

        # update calendar with streams
        for stream in formattedSchedule:
            if stream.description not in stream_ids:
                calendar.add_event(stream)