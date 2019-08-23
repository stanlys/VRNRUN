from django import forms
from django.forms import ModelForm
from trains.models import Trains,TrainsLog,TrainsList
from user.models import User,UnRegUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from datetime import datetime,timedelta
from django.forms import inlineformset_factory

def datetostr(day):
    rusmonth = ['Пустой',
                'Января',
                'Февраля',
                'Марта',
                'Апреля',
                'Мая',
                'Июня',
                'Июля',
                'Августа',
                'Сентября',
                'Октября',
                'Ноября',
                'Декабря']
    return day.strftime('%d {} %Y').format(rusmonth[int(day.strftime('%m'))])

def get_monday(day):
    # получить понедельник от указанной даты
    return day - timedelta(days=(day.isoweekday() - 1))

def get_friday(day):
    # получить пятницу от указанной даты
    return day + timedelta(days=(5 - day.isoweekday()))

def GetTrains(start, end, dayoftrains):
    daylist = []
    for d in range(int((end - start).days)):
        date = start + timedelta(d)
        if date.isoweekday() in dayoftrains:
            daylist.append(date)
    return daylist

def getdaytrain():
    days = []
    isdays = TrainsLog.objects.filter(istrain=True)
    for i in isdays:
        days.append(i.day)
    return days

def maketrainslist(d):
    days = [(datetostr(i), '{} в {}'.format(datetostr(i),TrainsLog.GetTime(TrainsLog,i.isoweekday()))) for i in GetTrains(datetime.now(), datetime.now() + timedelta(d), getdaytrain())]
    return days

class AddTrains(forms.Form):
    def __init__(self,*args, **kwargs):
        super(AddTrains, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.help_text_inline  = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-4'
        self.helper.add_input(Submit('send_button',u'Записаться'))

    first_name = forms.CharField(label='Ваше имя')
    second_name = forms.CharField(label='Ваша фамилия')
    phone = forms.CharField(label='Номер телефона')
    email = forms.EmailField(label='Ваш e-mail')
    day = maketrainslist(15)
    date2 = forms.ChoiceField(choices=day)
    # date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'} ))


    def save(self):
        print('Save - AddTrains')
        print(self.cleaned_data)
        #создаем нового незарегистрированного пользователя
        user1 = UnRegUser(first_name=self.cleaned_data['first_name'],
                          second_name=self.cleaned_data['second_name'],
                          phone=self.cleaned_data['phone'],
                          email=self.cleaned_data['email'],
                          )
        user1.save()
        #сохраняем тренировку в список тренировок
        train = TrainsList(trainsday=self.cleaned_data['date2'],unreguser=user1)
        train.save()


class ChooseTrainDate(forms.Form):

    def __init__(self, *args, **kwargs):
        super(ChooseTrainDate, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-4'
        self.helper.add_input(Submit('send_button', u'Далее'))

    ppp = TrainsLog.objects.filter(istrain=True)
    print(ppp)
    date = forms.IntegerField()

    def save(self):
        print('Save - ChooseTrainDate')


class IWANTRUN(forms.Form):
    pass
