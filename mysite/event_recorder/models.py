import datetime
from enum import Enum

from django.db import models
from django.dispatch.dispatcher import receiver
from django.utils import timezone
#from django.db.models.signals import post_delete

 
# Create your models here.
'''
Category([ID], name, parent)
Relation([ID], name)
Person([ID], first_name, last_name, relations, approx_DOB, gender)
Event([ID], start, end, description, categories, people)
Value([ID], event, enjoyment, productivity)
'''

class Category(models.Model): 
  '''
  Basic event category names, as well as parent category
  if applicable. Each category can only have one parent supercategory.
  (Having both parent and child attributes leads to information
  redundancy among rows.)
  Ex:   name              | parent            
        ----------------- | ----------------- 
        Inter-City Travel | Travel  
        Intra-City Travel | Travel
        Travel            |               
        Airfare           | Inter-City Travel
        Rail Train        | Inter-City Travel
        Bicycling         | Intra-City Travel
  '''
  name = models.CharField(max_length=100)
  #on_delete for parent attribute handled by category_post_delete_handler
  #Since Django's default behaviour is transactions aren't committed until
  #a request is completed, the post_delete handler will override on_delete
  parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL) 

  def __str__(self):
    return 'Name: {}; Parent: {}'.format(self.name, str(self.parent))
  
  class Meta:
    ordering = ('parent', 'name')

@receiver(models.signals.post_delete, sender=Category,
          dispatch_uid='string id for event category delete')
def category_post_delete_handler(sender, instance, **kwargs):
  ''' Update the parent attribute of all deleted category's children '''
  new_parent = instance.parent
  Category.objects.filter(parent_id=instance.id).update(
    parent=new_parent)


class Relation(models.Model):
  ''' Relation categories for Person model. '''
  name = models.CharField('Relationship Category', max_length = 50)

  def __str__(self):
    return self.name


class GenderChoices(Enum):
  M = 'Male'
  F = 'Female'
  O = 'LGBTQ'

#  @classmethod
#  def 
#    return tuple(x.name, x.value for x in )

class Person(models.Model):
  ''' Person with whom we can share an event experience. '''
  first_name = models.CharField(max_length =50)
  last_name = models.CharField(max_length = 50, blank=True)
  relations = models.ManyToManyField(Relation)
  approx_DOB = models.DateTimeField(null = True, blank=True)
  gender = models.CharField(max_length = 5, 
            #x is stored in database, x.value is human-readable
            choices = [(x.name, x.value) for x in GenderChoices],
            null=True
          )

  def __str__(self):
    return self.first_name + ' ' + self.last_name
  
  def getAge(self):
    if approx_DOB:
      return ((timezone.now() - self.approx_DOB).days)//365
    else:
      return -1

  class Meta:
    ordering = ('first_name', 'last_name')


class Event(models.Model):
  '''
  Basic event details including start time, end time, description. 
  Also includes two many-to-many relations with Category and Person.
  '''
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  description = models.CharField(max_length = 200)
  categories = models.ManyToManyField(Category)
  people = models.ManyToManyField(Person, blank=True)

  def __str__(self):
    return 'Event {}: '.format(str(self.id), self.description)
  
  def duration(self):
    return self.end - self.start #returns datetime.timedelta object
  
  def is_solo_event(self):
    return not self.people
  is_solo_event.admin_order_field = 'people'
  is_solo_event.boolean = True
  is_solo_event.short_description = 'Alone?'

  class Meta:
    ordering = ('-end_time', '-start_time')


class Value(models.Model):
  '''
  All the ratings (/10) associated with an event. Separate table
  for simplicity and also the fact that ratings usually aren't essential
  info.
  '''
  event = models.OneToOneField(Event, on_delete = models.CASCADE) 
  enjoyment = models.PositiveSmallIntegerField(
                'Enjoyment Rating', blank=True, null=True) #rating/10
  productivity = models.PositiveSmallIntegerField(
                'Productivity Rating', blank=True, null=True) #rating/10
  
  def __str__(self):
    return self.event.description + ': ' + str(self.enjoyment) + '; ' + \
      str(self.productivity)

  def overall_rating(self):
    total_score, denom = 0, 0
    if self.enjoyment:
      total_score += self.enjoyment
      denom += 10
    if self.productivity:
      total_score += self.productivity
      denom += 10
    return total_score/denom*10 if denom > 0 else None
  
  overall_rating.short_description = 'Overall Rating'



#TODO: Define a way to add Photo class : Photo([id], file_path, taken_date)
#TODO: After definining photos, add EventAndPhoto like EventAndCategory
#TODO: EventAndPhoto([ID], event, photo, is_thumbnail (bool) ) 
'''
class Photo
'''
