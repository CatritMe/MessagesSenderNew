from time import sleep

from django.apps import AppConfig

from mailing.management.commands.send import Command


class MailingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailing'
    verbose_name = 'Рассылки'

    def ready(self):
        sleep(2)
        Command().handle()
