from time import sleep

from flask import Flask, redirect, url_for
from celery import Celery
from flask_celery import make_celery


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
    task = add_together.delay(a=5, b=2)
    return f'<p>ansync request to add has been sent task id:</p><p>{task.id}</p>'
    

@celery.task()
def add_together(a, b):
    return a + b


if __name__ == '__main__':
    app.run(debug=True)