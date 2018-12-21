from django.contrib import admin
from .models import Category, Event, Relation, Person, Value

# Register your models here.
admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Relation)
admin.site.register(Person)
admin.site.register(Value)
