from apscheduler.schedulers.background import BackgroundScheduler
from django.core.management import BaseCommand
from mailing.services import send_mailing


class Command(BaseCommand):

    def handle(self, *args, **options):
        scheduler = BackgroundScheduler()
        scheduler.add_job(send_mailing, 'interval', seconds=10)
        scheduler.start()
