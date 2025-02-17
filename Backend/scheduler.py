import schedule
import time
import threading
from Backend.logger import logger

def run_continuously(interval=1):
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run

def start_scheduler(task):
    schedule.start_scheduler()

    schedule.every(3).minutes.do(task)

    # Continuously run
    stop_run_continuously = run_continuously()

    # Keep script alive
    try:
        while True:
            time.sleep(3600)
    except (KeyboardInterrupt, SystemExit):
        stop_run_continuously.set()