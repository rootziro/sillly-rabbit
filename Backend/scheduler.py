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

def start_scheduler(task, interval_minutes):
    schedule.start_scheduler()

    schedule.every(interval_minutes).minutes.do(task)

    # Continuously run
    stop_run_continuously = run_continuously()

    # Keep script alive
    try:
        while True:
            time.sleep(3600)
    except (KeyboardInterrupt, SystemExit):
        stop_run_continuously.set()

# Example task, please modify as needed
def Example_task():
    try:
        logger.info("Running Example Task")
        # Task logic here
    except Exception as e:
        logger.error(f"Error in Example Task: {e}")

if __name__ == "__main__":
# Get interval from user input / configuration
    interval_minutes = int(input("Enter interval in minutes: "))
    start_scheduler(Example_task, interval_minutes)