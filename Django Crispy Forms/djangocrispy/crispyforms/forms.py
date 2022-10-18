from django import forms
# from .models import *
from datetime import datetime
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



class UniversityForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action=reverse_lazy('index')
        self.helper.form_method='GET'
        self.helper.add_input(Submit('submit','Submit'))

    SUBJECT_CHOICES = (
        (1,'Web Development'),
        (2,'System Programming'),
        (3,"Data Science"),
        (4,'Software Developer')
    )

    Name = forms.CharField(widget=forms.TextInput(attrs={
        'hx-get': reverse_lazy('index'),
         'hx-trigger':'keyup'
    }))
    Email = forms.EmailField()
    Age = forms.IntegerField()
    Subject = forms.ChoiceField(
        choices=SUBJECT_CHOICES,
        widget=forms.RadioSelect()
    )
    Mobile_No = forms.IntegerField()
    DOB=forms.DateField(widget=forms.DateInput(attrs={'type':'date','max': datetime.now().date()}))