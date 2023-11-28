import datetime
from smtplib import SMTPException

from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail
from django.http import BadHeaderError

from config import settings


from mail_service.models import Messages, Logs
from mail_service.scheduler_job.jobs import mailing_day, mailing_week, mailing_month

messages = Messages.objects.all()
#setting = messages.setting



def start():
    for message in Messages.objects.all():

        setting = message.setting.regularity
        if message.status == 'К отправке':
            if setting == 'раз в день':
                hour_day = int(str(message.setting.time_mailing)[0:2])
                minute_day = int(str(message.setting.time_mailing)[3:5])
                date_start_day = message.setting.date_start
                date_stop_day = message.setting.date_stop
            elif setting == 'раз в неделю':
                hour_week = int(str(message.setting.time_mailing)[0:2])
                minute_week = int(str(message.setting.time_mailing)[3:5])
                date_start_week = message.setting.date_start
                date_stop_week = message.setting.date_stop
            elif setting == 'раз в месяц':
                hour_month = int(str(message.setting.time_mailing)[0:2])
                minute_month = int(str(message.setting.time_mailing)[3:5])
                date_start_mon = message.setting.date_start
                date_stop_mon = message.setting.date_stop

    scheduler_day = BackgroundScheduler(timezone='Europe/Moscow')
    scheduler_day.add_job(mailing_day, 'cron', day_of_week= '0-6',
                           hour= 13, minute= 45, start_date=date_start_day, end_date= date_stop_day)
    if scheduler_day.state == 0:
        scheduler_day.start()

    scheduler_week = BackgroundScheduler()
    scheduler_week.add_job(mailing_week, 'cron', week= '1-53', day= '1',
                           hour= hour_week, minute= minute_week, start_date=date_start_week, end_date= date_stop_week)
    if scheduler_week.state == 0:
        scheduler_week.start()

    scheduler_month = BackgroundScheduler()
    scheduler_month.add_job(mailing_month, 'cron', month='1-12', day=1,
                           hour= hour_month, minute= minute_month, start_date=date_start_mon, end_date= date_stop_mon)
    if scheduler_month.state == 0:
        scheduler_month.start()

