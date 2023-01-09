"""
This program is a CLI interface where the user can insert a time and a youtube
video will be played at that time as an alarm.
"""

# Import packages
import datetime
import os
import time
import random
import pafy
import vlc
import re

# Create a default video for the alarm
if not os.path.isfile('youtube_alarm_videos.txt'):
    print('Creating "youtube_alarm_videos.txt"...')
    with open('youtube_alarm_videos.txt', 'w') as f_alarm:
        f_alarm.write('https://www.youtube.com/watch?v=jWLMCwy4-ak')

with open('youtube_alarm_videos.txt', 'r') as url_alarm:
    url_list = url_alarm.readlines()

url = random.choice(url_list)
video = pafy.new(url)
# getting best stream
best = video.getbest()
media = vlc.MediaPlayer(best.url)

while True:
    # Create function to check that date and time are in the right format
    def check_date(current_date):
        # This function checks whether the date format has the right
        # formatting and whether the numbers are in the expecetd range.

        # Get current year
        now_year = datetime.datetime.today().year
        if type(current_date) != datetime.datetime:
            date = list(map(int, current_date.split('-')))
            dd = date[0]
            mm = date[1]
            user_date = datetime.datetime(now_year, mm, dd)


    def check_time(current_time):
        # This function checks whether the time format has the right
        # formatting and whether the numbers are in the expecetd range.
        if not re.match("[0-2][0-9]:[0-5][0-9]:[0-5][0-9]", current_time):
            raise ValueError('Wrong time format. Time must be (HH:MM:SS)')


    try:
        # Get date 
        date_in = input('\nInsert date of the alarm (dd-mm): ' or
                        datetime.date.today())
        # Check date format
        check_date(date_in)

        # Get time
        time_in = input('\nInsert time of the alarm (HH:MM:SS): ')
        # Check time format
        check_time(time_in)

        # Put date and time in a readible format.
        alarm_date1 = list(map(int, date_in.split('-')))
        current_year = datetime.date.today().year
        alarm_date = datetime.date(current_year, alarm_date1[1],
                                        alarm_date1[0])
        alarm_time1 = list(map(int, time_in.split(':')))
        alarm_time = datetime.time(alarm_time1[0], alarm_time1[1],
                                    alarm_time1[2]) 
        break
    except ValueError as e:
        print(e)
        continue


# Create a while loop that will run until the current time matches the time
# of the alarm
now = datetime.datetime.now()

while True:
    print(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"), end='\r')
    time.sleep(1)
    time_now = datetime.datetime.now().replace(microsecond=0).time()
    date_now = datetime.datetime.now().date()
    if alarm_time == time_now and alarm_date == date_now:
        media.play()
    else:
        continue

    prompt = input()
    if prompt == 'q':
        raise(KeyboardInterrupt)
