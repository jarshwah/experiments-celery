from celery import Celery
import time

app = Celery("tasks", broker="amqp://localhost")
app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Australia/Melbourne",
    enable_utc=True,
    acks_late=True,
)


@app.task
def sleepy(duration: int):
    print("Going to sleep")
    time.sleep(duration)
    print("Woke up")
    return None
