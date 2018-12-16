from django.contrib import admin

# Register your models here.
from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3

class QuestionAdmin(admin.ModelAdmin):
  #Editing how it looks as viewing all question info
  list_display = ('question_text', 'pub_date', 'was_published_recently')
  list_filter = ['pub_date']
  search_fields = ['question_text']

  #How each field looks when editing individual questions
  fieldsets = [
    (None,               {'fields': ['question_text']}),
    ('Date information', {'fields': ['pub_date']}),
  ]
  inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

