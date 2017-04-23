import time
import random
from celery import task
from tasks.models import Task

@task
def some_task(task_id):
    try:
        task = Task.objects.get(pk=task_id)
        task.status = "r"
        task.save()
        time.sleep(random.randint(0,10))
        task.status = "f"
        task.save()
    except Task.DoesNotExist:
        print('Task dees not exist in database!')
    