from django.db import models
from user.models import User,UnRegUser
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
class TrainsLog(models.Model):
    date = models.DateField(null=False,help_text='Дата проведения тренировки')
    comment = models.CharField(max_length=100, help_text = "Коментарий к тренировке")

    def __str__(self):
        return '{} - {}'.format(self.date.strftime('%Y-%m-%d'),self.comment[:20])

    class Meta:
        ordering = ["-date"]

#фактически записанные люди на тренировки
# информация для статистики
class TrainsList(models.Model):
    trains_id = models.ForeignKey(TrainsLog, on_delete=models.PROTECT)
    unreguser = models.ForeignKey(UnRegUser, on_delete=models.PROTECT)

    def __str__(self):
        return '{} - {}'.format(self.trains_id.date,self.unreguser.second_name)

    class Meta:
        ordering = ["-trains_id"]
