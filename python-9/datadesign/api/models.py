from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError

def validator_level(level):
    if level not in ['CRITICAL', 'DEBUG', 'ERROR', 'WARNING', 'INFO']:
        raise ValidationError(
            _('%(level) is not allowed'),
            params={'level': level},
        )

class Agent(models.Model):
    name = models.CharField('name', max_length = 50)
    status = models.BooleanField()
    env = models.CharField('env')
    version = models.CharField('version', max_length = 5)
    address = models.GenericIPAddressField('address', max_length = 39, protocol = 'IPv4') 

class User(models.Model):
    name = models.CharField('name', max_length = 50)
    last_login = models.DateTimeField('last_login', auto_now = True)
    email = models.CharField('email', max_length = 254, validators = [validators.EmailValidator()])
    password = models.CharField('password', max_length = 50, validators = [validators.MinLengthValidator(8)])

class Group(models.Model):
    name = models.CharField('name', max_length = 50)

class Event(models.Model):
    level = models.CharField('level', max_length = 20, validators=[validator_level])
    data = models.TextField('data')
    arquivado = models.BooleanField('arquivado')
    date = models.DateField('date', auto_now = True)
    agent = models.ForeignKey(Agent, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)