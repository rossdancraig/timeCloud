from django import forms
from .models import Category, Event, Person, Relation, Rating

class EventForm(forms.ModelForm):
  class Meta:
    model = Event
    fields = ['start_time', 'end_time', 'description']
  
