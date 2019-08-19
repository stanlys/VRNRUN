from django.db import models

# Create your models here.

class User(models.Model):
    strava_id = models.CharField(max_length=10,help_text='Stravas number user',default=0)
    first_name = models.CharField(max_length=30,help_text='User name')
    second_name = models.CharField(max_length=30,help_text='User second name')
    login = models.CharField(max_length=20,help_text='User login',default='')
    password = models.CharField(max_length=20,help_text='User password',default='')
    date_of_birth = models.DateField(null=True,help_text='Birthday')
    phone = models.CharField(max_length=15,help_text='User phone')
    email = models.CharField(max_length=50,help_text='User e-mail',default='mail@mail.ru')
    photo = models.ImageField()

    def __str__(self):
        return '({}) {} {}'.format(self.strava_id,self.first_name,self.second_name)


class UnRegUser(models.Model):
    first_name = models.CharField(max_length=30, help_text='User name')
    second_name = models.CharField(max_length=30, help_text='User second name')
    phone = models.CharField(max_length=15, help_text='User phone')
    email = models.CharField(max_length=50, help_text='User e-mail', default='mail@mail.ru')

    def __str__(self):
        return '{} {}'.format(self.first_name,self.second_name)