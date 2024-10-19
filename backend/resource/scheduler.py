from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from django.core.management import call_command
from resource.tasks import scan_for_data
from apscheduler.jobstores.base import JobLookupError

def run_my_command():
    try:
        # Your commands here
        call_command('absentees')
        call_command('task')
        call_command('mandays')
    except Exception as e:
        print(f"Error executing commands: {e}")

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    # Schedule the job to run every minute
    try:
        scheduler.add_job(run_my_command, trigger=IntervalTrigger(minutes=1), id="my_job", replace_existing=True)
    except JobLookupError:
        print("Job 'my_job' not found. Adding it again.")
        scheduler.add_job(run_my_command, trigger=IntervalTrigger(minutes=1), id="my_job")

    # Register the job and events
    register_events(scheduler)
    scheduler.start()
    print("Scheduler started.")

