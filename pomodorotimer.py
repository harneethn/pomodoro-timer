import time
import subprocess


alarmSound = 'alarm.mp3'

def playSound(file_path):
    try:
        subprocess.Popen(['afplay', file_path])
    except Exception as e:
        print(f"Error playing sound: {e}")

def displayAscii():
    asciiart = r'''
                          _______
                         | ___  o|
                         |[_-_]_ |
      ______________     |[_____]|
     |.------------.|    |[_____]|
     ||            ||    |[====o]|
     ||            ||    |[_.--_]|
     ||            ||    |[_____]|
     ||            ||    |       |
     ||____________||    | +===+ |
 .==.|""  ......    |.==.| _____ |
 |::| '-.________.-' |::|||_____||
 |''|  (__________)-.|''||_______|
 `""`_.............._\""`____
    /:::::::::::'':::\`;'-.-.`\
   /::=========.:.-::"\ \ \--\ \
   \`""""""""""""""""`/  \ \__) \
    `""""""""""""""""`    '======' 

'''
    print(asciiart + "\n")

def countdown(minutes, message):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02}:{:02}'.format(mins, secs)
        print(time_format, end='\r')
        time.sleep(1)
        seconds -= 1
    print(message)
    playSound(alarmSound)

def pomodoroTimer():
    workTime = int(input("enter your work time in minutes: "))
    breakTime = int(input("enter your break time in minutes: "))
    cycles = int(input("enter your prefered number of cycles: "))
    
    for i in range(cycles):
        displayAscii()
        print(f"work time {i+1}/{cycles}: {workTime} minutes")
        countdown(workTime, "times up")

    print(f"time for a break.")
    countdown(breakTime, "get back to work")

pomodoroTimer()