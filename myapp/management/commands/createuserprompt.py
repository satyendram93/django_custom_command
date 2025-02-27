from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.management.base import BaseCommand
import getpass

#Custom Command with prompt no arguments
class Command(BaseCommand):
    help="Create a normal user"
    
    def handle(self, *args, **kwargs):
        username = input('username: ')
        email = input('email: ')
        password = getpass.getpass('password: ')
        password2 = getpass.getpass('password (again): ')

        if password !=password2:
            self.stdout.write(self.style.ERROR('Error: your password did not match!'))
            return 
        try:
            validate_email(email)
        except ValidationError:
            self.stdout.write(self.style.ERROR('Error: Enter a valid email address!'))
            return 
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.ERROR('A user with that username already exists.'))
            return 

        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.ERROR('A user with that email already exists.'))
            return 

        try:
            User.objects.create_user(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'User {username} created successfully.'))
        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f'Error: {e.message_dict}'))
        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
    