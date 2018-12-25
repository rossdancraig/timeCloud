from django import forms
#from django.forms.widgets import CheckboxSelectMultiple
from .models import Category, Event, Person, Relation, Rating

class EventForm(forms.ModelForm):
  class Meta:
    model = Event
#    categories = CheckboxSelectMultiple(required=False)
    fields = ['start_time', 'end_time', 'description', 'categories']
#    categories = forms.MultipleChoiceField(
#      retuired=False,
#      widget = forms.CheckboxSelectMultiple)

  def __init__(self, *args, **kwargs):
    
    super(EventForm, self).__init__(*args, **kwargs)
    
    self.fields['categories'].widget = forms.widgets.CheckboxSelectMultiple()
    self.fields['categories'].queryset = Category.objects.all()
    self.fields['categories'].required = False
  
