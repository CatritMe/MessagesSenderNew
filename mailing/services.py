import smtplib
from datetime import datetime, timedelta

import pytz
from django.core.mail import send_mail
from django.db.models import F

from config import settings
from mailing.models import Mailing, MailingAttempt


def send_mailing():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    # создание объекта с применением фильтра
    mailings = Mailing.objects.filter(sent_time__lte=current_datetime)
    for mailing in mailings:
        try:
            send_mail(
                subject=mailing.mail.topic,
                message=mailing.mail.text,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email for client in mailing.client.all()]
            )
            if mailing.periodicity == 'DY':
                mailing.sent_time = F('sent_time') + timedelta(days=1)
                mailing.status = 'запущена'
            elif mailing.periodicity == 'WK':
                mailing.sent_time = F('sent_time') + timedelta(days=7)
                mailing.status = 'запущена'
            elif mailing.periodicity == 'MN':
                mailing.sent_time = F('sent_time') + timedelta(days=30)
                mailing.status = 'запущена'
            mailing.save()
            is_success = True
            server_response = 'успешно'
            MailingAttempt.objects.create(mailing=mailing, is_success=is_success, answer=server_response)

        except smtplib.SMTPResponseException as error:
            is_success = False
            server_response = str(error)
            MailingAttempt.objects.create(mailing=mailing, is_success=is_success, answer=server_response)
