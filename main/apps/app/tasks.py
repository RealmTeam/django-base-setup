# -*- coding: utf-8 -*-
"""This module should contain asynchronous tasks executed by celery"""

from celery import shared_task


# @shared_task
# def add(a, b):
#     return a + b

# # Simple tasks usage
# result = add(1 + 2)  # We can simply call the function.
# task = add.delay(1 + 2)  # Or we can send it to a task
# task = celery.current_app.AsyncResult(task.id)  # We can find a task by its id
# if task.ready():  # We can check if it's ready
# if task.successful():  # successful
# if task.failed():  # or if it has failed
# result = task.get()  # Then we can get the result
