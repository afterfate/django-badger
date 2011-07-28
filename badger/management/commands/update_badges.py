from os.path import dirname, basename

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.db.models import get_apps, get_models, signals
from django.utils.importlib import import_module

from badger.models import Badge, Nomination, Award
from badger.management import update_badges

class Command(BaseCommand):
    args = ''
    help = 'Update badges from apps'

    def handle(self, *args, **options):
        update_badges()