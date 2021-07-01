from django.core.management.base import BaseCommand
import logging

cron_logger = logging.getLogger('cron_logger')


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-date', nargs="+", type=str, help="Data populate date range")

    def handle(self, *args, **options):
        try:
            self.date = options["date"][0]
        except:
            self.date = "today"
        

    def info(self, message):
        print(message)
        cron_logger.info(message)

    def error(self, message):
        print(message)
        cron_logger.error(message, exc_info=True)
        
