from django import forms
from trains.models import Trains
from user.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from datetime import date

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
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'} ))

    def save(self):
        print(self.cleaned_data)
        user1 = User(first_name='Сергей')
        print(user1)
        print('user ready')
        user1.save()
        train = Trains(date=self.cleaned_data['date'], users=user1)
        print('train ready')
        train.save()
        return train




