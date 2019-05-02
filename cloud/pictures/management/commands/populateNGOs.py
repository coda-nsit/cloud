from django.core.management.base import BaseCommand, CommandError
from pictures.models import NGO 



class Command(BaseCommand):
    # def add_arguments(self, parser):
    #     parser.add_argument('number', type=int)

    def handle(self, *args, **options):
        number = 10
        for i in range(number):
            NGO.objects.create(id=i)
             