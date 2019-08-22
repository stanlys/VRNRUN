from django import forms
from django.forms import ModelForm
from trains.models import Trains
from user.models import User,UnRegUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from datetime import date
from django.forms import inlineformset_factory




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
    # date2 = forms.ChoiceField()
    # date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'} ))

    def save(self):
        print('Save - AddTrains')
        # print(self.cleaned_data)
        # user1 = User(first_name='Сергей')
        # print(user1)
        # print('user ready')
        # user1.save()
        # train = Trains(date=self.cleaned_data['date'], users=user1)
        # print('train ready')
        # train.save()
        # return train


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

    date_choices=(
        (date(2019, 8, 22), '22 августа 2019 года'),
        (date(2019, 8, 24), '24 августа 2019 года'),
        (date(2019, 8, 27), '27 августа 2019 года')
    )

    date = forms.ChoiceField(choices=date_choices)

    def save(self):
        print('Save - ChooseTrainDate')



class IWANTRUN(forms.Form):
    pass
