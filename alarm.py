import datetime
import time
def set_time():
    while True:
        try:
            set_time = input('What time do you want to set?(hh:mm AM/PM)')
            set_time = set_time.replace(' ','')
            set_time = datetime.datetime.strptime(set_time, '%I:%M%p')
            set_time = set_time.time()
            return set_time
        except ValueError:
            print(f'{set_time} is not an valid input')
            continue
        
def current_time():
    currenthour = str(datetime.datetime.now().hour)
    currentminute = str(datetime.datetime.now().minute)
    now = datetime.datetime.strptime(f'{currenthour}:{currentminute}', '%H:%M')
    now = now.time()
    return now

inputtime = set_time()
while True:
    if inputtime <= current_time():
        print('Alarm!')
        break
    time.sleep(30)