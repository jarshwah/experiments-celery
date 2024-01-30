# experiments-celery

A repo with celery configured for running experiments and debugging

## Setup

1. Install [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/)
2. Setup a virtual environment with python 3.10+ and install the requirements
3. Start the rabbitmq server: `./start-rmq.sh`
4. Start the celery worker: `./start-celery.sh`
5. Open a python shell and start some tasks up:

```python
from tasks import sleepy

sleepy.delay(10)
sleepy.apply_async((10,), countdown=20)
```

If you want to play with the behaviour of SIGTERM, find the PID of the celery
parent task, and `kill -TERM <pid>`.

ddtrace-run is used here as I was experimenting with how it may or may not affect
the behaviour of the kill signal, but ddtrace-run doesn't act as a parent process
and so does not impact TERM at all.
