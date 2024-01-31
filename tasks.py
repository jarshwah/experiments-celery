from celery import Celery
import time

app = Celery("tasks", broker="pyamqp://localhost")
app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Australia/Melbourne",
    enable_utc=True,
    task_acks_late=True,
    task_acks_on_failure_or_timeout=False,
)


@app.task
def sleepy(duration: int):
    print("Going to sleep")
    time.sleep(duration)
    print("Woke up")
    return None
