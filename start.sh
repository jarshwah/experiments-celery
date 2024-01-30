#!bin/sh
ddtrace-run celery --app=tasks.app worker --loglevel=info --concurrency=4 --without-heartbeat --without-gossip --without-mingle
