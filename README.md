# Twitch-Google-Calendar
Collects the twitch schedules of streamers and enters them as events in a google calendar

*I realize this is very janky and cobbled together code, you have no obligation to run this code on your computer*

# Setup
## Twitch Authorization
1) Login to your twitch console
2) Click on "Register your application"
3) Name "Twitch Schedule Consolidator" recommended but enter whatever you want so that you remember what this is when you look at this later in the future
4) For category, select "other"
5) Copy client id and client secret into a json file
`{
"client_id":"your client id here",
"client_secret":"your client secret here"
}`
6) Save

## Google API
7) Go to [Google Python Quickstart](https://developers.google.com/calendar/api/quickstart/python) and follow the instructions
8) Copy the credentials.json file into the same folder as this project

9) Done
