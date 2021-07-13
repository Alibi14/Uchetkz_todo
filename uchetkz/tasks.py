from celery import shared_task
from django.core.mail import send_mail
from uchetkz.celery import app


@app.task
def email_send(email):
    send_mail(
        'Uchetkz',
        "It's your task",
        'alibi9191@gmail.com',
        [email],
        fail_silently=False
    )
