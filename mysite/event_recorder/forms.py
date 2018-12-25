from django import forms
#from django.forms.widgets import CheckboxSelectMultiple
from .models import Category, Event, Person, Relation, Rating

class EventForm(forms.ModelForm):
  class Meta:
    model = Event
    fields = ['start_time', 'end_time', 'description', 
              'categories', 'people']

  def __init__(self, *args, **kwargs):
    
    super(EventForm, self).__init__(*args, **kwargs)
    
    self.fields['categories'].widget = forms.widgets.CheckboxSelectMultiple()
    self.fields['categories'].queryset = Category.objects.all()
    self.fields['categories'].required = False
  
    self.fields['people'].widget = forms.widgets.CheckboxSelectMultiple()
    self.fields['people'].queryset = Person.objects.all()
    self.fields['people'].required = False
  

class CategoryForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = ['name', 'parent']

  def __init__(self, *args, **kwargs):
    
    super(CategoryForm, self).__init__(*args, **kwargs)
    
    self.fields['parent'].required = False
  

class PersonForm(forms.ModelForm):
  class Meta:
    model = Person
    fields = ['first_name', 'last_name', 'relations', 
              'approx_DOB', 'gender']

  def __init__(self, *args, **kwargs):
    
    super(PersonForm, self).__init__(*args, **kwargs)
    
    self.fields['relations'].widget = forms.widgets.CheckboxSelectMultiple()
    self.fields['relations'].queryset = Relation.objects.all()
    self.fields['relations'].required = False
  
    self.fields['gender'].required = False
    self.fields['approx_DOB'].required = False
