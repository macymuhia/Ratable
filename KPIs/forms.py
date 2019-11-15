from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class AddArea(forms.ModelForm):
  class Meta:
    model = Area
    fields = ['name']


class AddIndicator(forms.ModelForm):
  class Meta:
    model = Indicators
    fields = ['name', 'area']


class GiveScore(forms.Form):
  SCORE_CHOICES = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
  ]
  
  score = forms.RadioSelect(choices=SCORE_CHOICES)

  def save_score(self):
    self.save()