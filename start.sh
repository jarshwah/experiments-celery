celery --app=tasks.app worker --loglevel=info --concurrency=2 --without-heartbeat --without-gossip --without-mingle
