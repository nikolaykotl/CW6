from smtplib import SMTPException

from django.core.mail import send_mail
from django.http import BadHeaderError

from config import settings
from mail_service.models import Messages, Logs


#from mail_service.scheduler_job.updater import message

def mailing_day():
    for message in Messages.objects.all():

        setting = message.setting.regularity
        if message.status == 'К отправке' and message.is_active and message.user.is_block != True:
            if setting == 'раз в день':
                clients = message.clients.all()
                if clients != []:
                    client_list = ",".join(str(x) for x in clients)
                    client_email = client_list.split(',')
                    try:
                        for email in client_email:
                            send_mail(
                                message.title,
                                message.body,
                                from_email=settings.EMAIL_HOST_USER,
                                recipient_list=[email],
                                fail_silently=False,
                            )
                            print(email, setting, client_email , message.setting.date_start, message.date_create, message.setting.date_stop)
                            for client in clients:
                                Logs.objects.create(
                                    message=message,
                                    client=client,
                                    status=Logs.STATUS_OK,
                                )

                    except BadHeaderError as e:
                        print("Произошла ошибка BadHeaderError при отправке письма:", str(e))
                        Logs.objects.create(
                            message=message,
                            client=client,
                            status=Logs.STATUS_FAILED,
                            server_response="BadHeaderError: " + str(e),
                        )

                    except SMTPException as e:
                        print("Произошла ошибка SMTP при отправке письма:", str(e))
                        Logs.objects.create(
                            message=message,
                            client=client,
                            status=Logs.STATUS_FAILED,
                            server_response="SMTPException: " + str(e),
                        )

def mailing_week():
    for message in Messages.objects.all():
        setting = message.setting.regularity
        if message.status == 'К отправке' and message.is_active and message.user.is_block != True:
            if setting == 'раз в неделю':
                clients = message.clients.all()
                if clients != []:
                    client_list = ",".join(str(x) for x in clients)
                    client_email = client_list.split(',')
                    try:
                        for email in client_email:
                            send_mail(
                                message.title,
                                message.body,
                                from_email=settings.EMAIL_HOST_USER,
                                recipient_list=[email],
                                fail_silently=False,
                            )
                            print(email, setting)
                            for client in clients:
                                Logs.objects.create(
                                    message=message,
                                    client=client,
                                    status=Logs.STATUS_OK,
                                )

                    except BadHeaderError as e:
                        print("Произошла ошибка BadHeaderError при отправке письма:", str(e))
                        Logs.objects.create(
                            message=message,
                            client=client,
                            status=Logs.STATUS_FAILED,
                            server_response="BadHeaderError: " + str(e),
                        )

                    except SMTPException as e:
                        print("Произошла ошибка SMTP при отправке письма:", str(e))
                        Logs.objects.create(
                            message=message,
                            client=client,
                            status=Logs.STATUS_FAILED,
                            server_response="SMTPException: " + str(e),
                        )
def mailing_month():
    for message in Messages.objects.all():
        setting = message.setting.regularity
        if message.status == 'К отправке' and message.is_active and message.user.is_block != True:
            if setting == 'раз в месяц':
                clients = message.clients.all()
                if clients != []:
                    client_list = ",".join(str(x) for x in clients)
                    client_email = client_list.split(',')
                    try:
                        for email in client_email:
                            send_mail(
                                message.title,
                                message.body,
                                from_email=settings.EMAIL_HOST_USER,
                                recipient_list=[email],
                                fail_silently=False,
                            )
                            print(email, setting)
                            for client in clients:
                                Logs.objects.create(
                                    message=message,
                                    client=client,
                                    status=Logs.STATUS_OK,
                                )

                    except BadHeaderError as e:
                        print("Произошла ошибка BadHeaderError при отправке письма:", str(e))
                        Logs.objects.create(
                            message=message,
                            client=client,
                            status=Logs.STATUS_FAILED,
                            server_response="BadHeaderError: " + str(e),
                        )

                    except SMTPException as e:
                        print("Произошла ошибка SMTP при отправке письма:", str(e))
                        Logs.objects.create(
                            message=message,
                            client=client,
                            status=Logs.STATUS_FAILED,
                            server_response="SMTPException: " + str(e),
                        )