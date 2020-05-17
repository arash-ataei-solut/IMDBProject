from __future__ import absolute_import, unicode_literals

import smtplib
from email.message import EmailMessage

from celery import shared_task
from django.contrib.auth.models import User

from movie.models.models import Movie


@shared_task
def send_email(user_id, movie_id, text):
    user = User.objects.get(id=user_id)
    movie = Movie.objects.get(id=movie_id)

    interested_users = User.objects.filter(rates__movie=movie)
    if interested_users:
        for i in interested_users:
            if i.email:
                msg = EmailMessage()
                msg.set_content('{} said about the movie {}: {}'.format(user.username, movie.name, text))
                msg['Subject'] = 'review'
                msg['From'] = ''
                msg['To'] = i.email
                try:
                    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.ehlo()
                    server.login("sender_email", "sender_password")
                    to_email = i.email
                    message = msg.as_string()
                    server.sendmail('sender_email', to_email, message)
                except Exception as e:
                    print(e)
