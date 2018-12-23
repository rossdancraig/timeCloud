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
  name = models.CharField(max_length=100, unique=False,
          null=False, blank=False) 
  #on_delete for parent attribute handled by category_post_delete_handler
  #Since Django's default behaviour is transactions aren't committed until
  #a request is completed, the post_delete handler will override on_delete
  parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL) 

  def __str__(self):
    return '{}-{}'.format(self.id, self.name)
  
  class Meta:
    ordering = [models.F('parent').asc(nulls_first=True), 'name']#, 'name')

@receiver(models.signals.post_delete, sender=Category,
          dispatch_uid='string id for event category delete')
def category_post_delete_handler(sender, instance, **kwargs):
  ''' Update the parent attribute of all deleted category's children '''
  new_parent = instance.parent
  Category.objects.filter(parent_id=instance.id).update(
    parent=new_parent)


class Relation(models.Model):
  ''' Relation categories for Person model. '''
  name = models.CharField('Relationship Category', max_length = 50, 
          blank=False, null=False)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ('name',)


class GenderChoices(Enum):
  M = 'Male'
  F = 'Female'
  O = 'LGBTQ'

#  @classmethod
#  def 
#    return tuple(x.name, x.value for x in )

class Person(models.Model):
  ''' Person with whom we can share an event experience. '''
  first_name = models.CharField(max_length =50,
                blank=False, null=False)
  last_name = models.CharField(max_length = 50, blank=True)
  relations = models.ManyToManyField(Relation)
  approx_DOB = models.DateTimeField(null = True, blank=True)
  gender = models.CharField(max_length = 1, 
            #x.name is stored in database, x.value is human-readable
            choices = [(x.name, x.value) for x in GenderChoices],
            null=True,
          )

  def __str__(self):
    return self.first_name + ' ' + self.last_name
  
  def getAge(self):
    if self.approx_DOB:
      return ((timezone.now() - self.approx_DOB).days)//365
    else:
      return -1

  class Meta:
    ordering = ('first_name', 'last_name')


class Event(models.Model):
  '''
  Basic event details including start time, end time, description. 
  Also includes two many-to-many relations with Category and Person.
  Finally, includes a notes section in case you want to write about
  the event more in detail (max about 200 words).
  '''
  start_time = models.DateTimeField()
  end_time = models.DateTimeField(null=True)
  description = models.CharField(max_length = 200, blank=True)
  categories = models.ManyToManyField(Category)
  people = models.ManyToManyField(Person)
  notes = models.CharField(max_length = 1000, blank=True)

  def __str__(self):
    return '{}: {}'.format(str(self.id), self.description)
  
  def duration(self):
    end = self.end_time if self.end_time else timezone.now()
    return end - self.start_time #datetime.timedelta object
  
  def is_solo_event(self):
    return self.people.get_queryset().count() == 0
  is_solo_event.admin_order_field = 'people'
  is_solo_event.boolean = True
  is_solo_event.short_description = 'Alone?'

  class Meta:
    ordering = ('-end_time', '-start_time')


class Rating(models.Model):
  '''
  All the ratings (/10) associated with an event. Separate table
  for simplicity and also the fact that people usually just care
  about the overall rating instead of individual scores.
  '''
  event = models.OneToOneField(Event, null=False,
            on_delete = models.CASCADE) 
  enjoyment = models.PositiveSmallIntegerField(
                'Enjoyment Rating', blank=True, null=True) #rating/10
  productivity = models.PositiveSmallIntegerField(
                'Productivity Rating', blank=True, null=True) #rating/10
  
  def __str__(self):
    return '{} ({}) - {} - {}'.format(str(self.event.id), 
      self.event.description, str(self.enjoyment), str(self.productivity))

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
