# Flask + Celery + Redis + Windows

### What could go wrong


After a day of trying to launch redis & celery worker and launching tasks asynch, feel like saving the progress...


worker works with command:

`celery -A app.celery worker -P eventlet --loglevel=info`

and settings:

`
    'broker_url': 'redis://127.0.0.1:6379',
    'result_backend': 'redis://127.0.0.1:6379'
`

Special thanks for celery devs not accepting `localhost` and wasting my time until I found [you cant use it](https://stackoverflow.com/a/59738036/11537568)

## Requirements / Prerequisites:

- pipenv install -r requirements.txt
- extract and run `redis-server.exe` in wherever

## Redis zip of binaries includes:
- redis-benchmark.exe
- redis-check-aof.exe
- redis-check-dump.exe
- redis-cli.exe
- redis-server.exe
