from django.db import models
from user.models import User,UnRegUser
from datetime import timedelta

# Create your models here.

class Trains(models.Model):
    date = models.DateField(null=False)
    users = models.ForeignKey(User , on_delete=models.PROTECT)

    def __str__(self):
        return '{} - {}'.format(self.date,self.users.login)

    class Meta:
        get_latest_by = 'date'
        ordering=['-date','users']

#Журнал тренировок, заполняет администратор сайта
# в дальнейшем попробуем автоматизировать заполнение по дням недели
# тренировки будут проходить во вторник, четвер и воскресенье
#1 - понедельник, 7 -воскресенье
class TrainsLog(models.Model):
    dayweek = ['Ближайщая','Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']
    day = models.IntegerField(null=False,help_text='Номер дня недели проведения тренировки')
    time = models.TimeField(help_text='Время проведения тренировки')
    istrain = models.BooleanField(null=False,help_text='Будет ли в этот день тренировка')
    comment = models.CharField(max_length=100, help_text = "Коментарий к тренировке")

    def __str__(self):
        return u'{} {} - {}'.format(self.dayweek[self.day],self.time,self.istrain)

    class Meta:
        ordering = ["-day"]

    def GetTime(self,index):
        temp = self.objects.get(day=index)
        return temp.time.strftime('%R')

#фактически записанные люди на тренировки
# информация для статистики
class TrainsList(models.Model):
    trainsday = models.DateField(help_text='Дата тренировки')
    unreguser = models.ForeignKey(UnRegUser, on_delete=models.PROTECT)

    def __str__(self):
        return '{} - {}'.format(self.trainsday, self.unreguser.second_name)

    class Meta:
        ordering = ["-trainsday"]


#список тренеров и администрации
class Trener(models.Model):
    FIO = models.CharField(max_length=50,help_text='ФИО отвественного человека')
    description = models.TextField(help_text='Описание обязанностей')
    isshow = models.BooleanField(help_text='Показывать на главной странице')
    image= models.ImageField(verbose_name='Изображение',help_text='Фотография')

    def __str__(self):
        return "{} {}".format(self.FIO,str(self.isshow))