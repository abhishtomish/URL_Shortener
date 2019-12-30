from django.core.management.base import BaseCommand, CommandError
from shortener.models import Shorten_URL

class Command(BaseCommand):
    help = "Refresh all short URLs"

    def handle(self, *args, **options):
        return Shorten_URL.objects.refresh_shorturl()