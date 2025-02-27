from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Print a message to the console.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Hello Django from Terminal!'))