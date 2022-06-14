from time import sleep
from flask import Flask, url_for
from flask_celery import make_celery


app = Flask(__name__)
app.config.update(CELERY_CONFIG={
    'broker_url': 'redis://127.0.0.1:6379',
    'result_backend': 'redis://127.0.0.1:6379',
})
celery = make_celery(app)

# --------- TASKS ---------
@celery.task()
def add_together(a, b):
    return a + b

@celery.task()
def computationaly_fake():
    sleep(20)
    return {'msg':'LE RESULT'}


# --------- ROUTES ---------
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


if __name__ == '__main__':
    app.run(debug=True)