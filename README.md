# Twitch-Google-Calendar
Collects the twitch schedules of streamers and enters them as events in a google calendar

*I realize this is very janky and cobbled together code, you have no obligation to run this code on your computer*

# Setup
## Twitch Authorization
1) Login to your twitch console
2) Click on "Register your application"
3) Name "Twitch Schedule Consolidator" recommended but enter whatever you want so that you remember what this is when you look at this later in the future
4) For category, select "other"
5) Copy client id and client secret into a json file named "twitch_secrets.json"
example: `{"client_id":"your client id here","client_secret":"your client secret here"}`
6) Save

## Creating streamers list
7) create a json file called "streamers.json"
example: `{"streamers":["streamer name 1","streamer name 2", "streamer name 3"]}`

## Google API
8) Go to [Google Python Quickstart](https://developers.google.com/calendar/api/quickstart/python) and follow the instructions
9) Copy the credentials.json file into the same folder as this project

## Google Calendar
10)  Create or choose the google calendar you want the program to put the stream events and click on the 3 dots next to and click "Settings and sharing"
11) Scroll down to "Integrate Calendar" and copy the calendar id into a json file similar to the format shown above named "google_secrets.json"
example: `{"google_secret":"you calendar id here"}`

12) Done
