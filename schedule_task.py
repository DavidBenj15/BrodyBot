import schedule
import time
import subprocess

def run_daily_task():
    subprocess.Popen(['python', 'main.py'])
    time.sleep(30)
    subprocess.Popen(['python', 'main.py'])
    time.sleep(30)
    subprocess.Popen(['python', 'main.py'])
    print("Task running")

schedule.every().day.at("23:59:57").do(run_daily_task)
print("Running schedule_task.py")

while True:
    schedule.run_pending()
    time.sleep(1) # check every ... seconds
