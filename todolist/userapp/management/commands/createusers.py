from django.core.management import BaseCommand
from userapp.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.all().delete()
        User.objects.create_superuser(username='nanku',
                                            email='sana9056@yandex.ru',
                                            password='9056')
        User.objects.create_user(username='test',
                                       email='test123@test.com',
                                       password='123',
                                       )
        User.objects.create_user(username='test1',
                                       email='test1234@test.com',
                                       password='1234',
                                       )
