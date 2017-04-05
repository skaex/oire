import re
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import Group
from accounts.models import User


class Command(BaseCommand):
    help = 'Prepares and creates a test user for reviewing the system'

    def handle(self, *args, **options):
        try:
            email = input('Please provide your email: ')
            while not re.match(r'[a-zA-Z0-9.]{3,}@[a-zA-Z0-9.]{2,}', email):
                self.stderr.write("Error: Please provide a valid email: ")
                email = input('Please provide your email: ')
            password = input('Please provide a password: ')
            re_password = input('Please confirm the password: ')
            while len(password) < 5 and password != re_password:
                if password != re_password:
                    self.stderr.write("Error: Please make sure the password and the confirmation match: ")
                if len(password) < 5:
                    self.stderr.write("Error: Please make sure the password is more than 4 characters ")
                password = input('Please provide a password: ')
                re_password = input('Please confirm the password: ')

            self.stdout.write("Creating a goat: %s" % email)
            call_command('makemigrations')
            call_command('migrate')
            call_command('loaddata', 'groups')
            goat = User.objects.create_user(username=email.split('@')[0], email=email, password=password, is_superuser=True)
            goat.groups.add(Group.objects.get(name="Administrator"))
            self.stdout.write(self.style.SUCCESS("Goat created: %s" % goat.email))
        except KeyboardInterrupt:
            self.stderr.write("\nOperation Aborted!")