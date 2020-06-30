import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is avail"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting or database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, wiating 1s...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
