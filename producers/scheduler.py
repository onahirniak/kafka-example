import schedule
import time

class Scheduler():
    
    @staticmethod
    def run(seconds, job):

        schedule.every(seconds).seconds.do(job)

        while True:
            schedule.run_pending()
            time.sleep(1)