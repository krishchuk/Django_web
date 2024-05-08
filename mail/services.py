from datetime import datetime, timedelta
from smtplib import SMTPException

import pytz
from django.core.cache import cache

from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

from blog.models import Blog
from mail.models import EmailSettings, EmailTry, Client


def my_job():
    day = timedelta(days=1, hours=0, minutes=0)
    weak = timedelta(days=7, hours=0, minutes=0)
    month = timedelta(days=30, hours=0, minutes=0)
    year = timedelta(days=365, hours=0, minutes=0)

    mails = EmailSettings.objects.all().filter(status='CREATED') \
        .filter(is_active=True) \
        .filter(date_next__lte=timezone.now()) \
        .filter(date_end__gte=timezone.now())

    for mail in mails:
        mail.status = 'RUN'
        mail.save()
        emails_list = [client.email for client in mail.clients.all()]

        result = send_mail(
            subject=mail.message.head,
            message=mail.message.body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=emails_list,
            fail_silently=False,
        )

        if result == 1:
            status = True
        else:
            status = False

        log = EmailTry(mailing=mail, try_status=status)
        log.save()

        if mail.periodicity == 'PD':
            mail.next_date = log.last_try_datetime + day
        elif mail.periodicity == 'PW':
            mail.next_date = log.last_try_datetime + weak
        elif mail.periodicity == 'PM':
            mail.next_date = log.last_try_datetime + month
        elif mail.periodicity == 'PY':
            mail.next_date = log.last_try_datetime + year

        if mail.next_date < mail.date_end:
            mail.status = 'CREATED'
        else:
            mail.status = 'CLOSE'
        mail.save()


def get_blog_from_cache():
    if not settings.CACHE_ENABLED:
        return Blog.objects.all()
    key = "blog_list"
    blog = cache.get(key)
    if blog is not None:
        return blog
    blog = Blog.objects.all()
    cache.set(key, blog)
    return blog


def get_clients_count_from_cache():
    if not settings.CACHE_ENABLED:
        return Client.objects.all().values('email').distinct().count()
    key = "unique_clients_count"
    unique_clients_count = cache.get(key)
    if unique_clients_count is not None:
        return unique_clients_count
    unique_clients_count = Client.objects.all().values('email').distinct().count()
    cache.set(key, unique_clients_count)
    return unique_clients_count


def get_all_mailings_count_from_cache():
    if not settings.CACHE_ENABLED:
        return EmailSettings.objects.all().count()
    key = "active_mailings_count"
    all_mailings_count = cache.get(key)
    if all_mailings_count is not None:
        return all_mailings_count
    all_mailings_count = EmailSettings.objects.all().count()
    cache.set(key, all_mailings_count)
    return all_mailings_count


def get_active_mailings_count_from_cache():
    if not settings.CACHE_ENABLED:
        return EmailSettings.objects.all().filter(is_active=True).count()
    key = "active_mailings_count"
    active_mailings_count = cache.get(key)
    if active_mailings_count is not None:
        return active_mailings_count
    active_mailings_count = EmailSettings.objects.all().filter(is_active=True).count()
    cache.set(key, active_mailings_count)
    return active_mailings_count


def send_mailing():
    current_time = timezone.localtime(timezone.now())
    mailing_list = EmailSettings.objects.all()
    for mailing in mailing_list:
        if mailing.date_end < current_time:
            mailing.status = EmailSettings.DONE
            continue
        if mailing.time_start <= current_time < mailing.date_end:
            mailing.status = EmailSettings.STARTED
            mailing.save()
            for client in mailing.client.all():
                try:
                    send_mail(
                        subject=mailing.message.head,
                        message=mailing.message.body,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[client.email],
                        fail_silently=False
                    )

                    log = EmailTry.objects.create(
                        date=mailing.start_time,
                        status=EmailTry.SENT,
                        mailing=mailing,
                        client=client
                    )
                    log.save()
                    return log

                except SMTPException as error:
                    log = EmailTry.objects.create(
                        date=mailing.start_time,
                        status=EmailTry.FAILED,
                        mailling=mailing,
                        client=client,
                        response=error
                    )
                    log.save()

                    return log

        else:
            mailing.status = EmailSettings.DONE
            mailing.save()
