from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@example.com',
            name='admin',
            telegram_chat_id='1234567',
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )
        user.set_password('qwe123qwe')
        user.save()
