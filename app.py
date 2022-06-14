from time import sleep

from flask import Flask, redirect, url_for
from celery import Celery
from flask_celery import make_celery
# from celery.result import AsyncResult


app = Flask(__name__)
app.config.update(CELERY_CONFIG={
    'broker_url': 'redis://127.0.0.1:6379',
    'result_backend': 'redis://127.0.0.1:6379',
})

celery = make_celery(app)


@celery.task()
def add_together(a, b):
    return a + b


@app.route('/')
def index():
    # task = add_together.delay(a=5, b=2)
    task = computationaly_fake.delay()
    return f'''<p>ansync request to add has been sent.
        Task id:</p><p>{task.id}</p><br>
        <a href="{url_for('status', task_id=task.id)}">Check result<a>'''
    
@app.route('/status/<task_id>')
def status(task_id):
    task = celery.AsyncResult(task_id)
    if task.ready():
        return f'<p>Finished executing function. Result:</p><p>{task.result["msg"]}</p>'
    else:
        return f'Your task is being processed. Current status: {task.status}'

@celery.task()
def add_together(a, b):
    return a + b

@celery.task()
def computationaly_fake():
    sleep(20)
    return {'msg':'LE RESULT'}


if __name__ == '__main__':
    app.run(debug=True)