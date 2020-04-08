from django.contrib.auth.models import AbstractUser
from django.db import models


#This class is for customizing custom user model.
#default field: user_name, first_name, last_name, email, password, groups, etc.
#ex) we can add age field, company field, etc.
class CustomUser(AbstractUser):
    '''when you add nes fields, you must implement following command.
    $ python manage.py makemigrations [app name(ex. guests)]
    $ python manage.py migrate
    '''
    age = models.PositiveIntegerField(null=True,blank=True)
    country = models.CharField(max_length=20,null=True,blank=True)