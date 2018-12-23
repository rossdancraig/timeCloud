from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic 

from .models import Category, Event, Person, Relation, Value

class IndexView(generic.ListView):
  template_name = 'main/index.html'
  context_object_name = 'main_page'

  def get_queryset(self):
    return None

def EventIndexView(request, *args, **kwargs):
  print(args, kwargs)
  print(request.user)
  context = {'events_list': []}
  events = Event.objects.all()
  for event in events:
    event_info = [event, (event.categories.all()), 
                  (event.people.all())]
    if hasattr(event, 'value'):
      event_info.append((event.value.overall_rating()))
    else:
      event_info.append('')
    context['events_list'].append(event_info)
  return render(request, 'events/index.html', context)

class EventDetailView(generic.DetailView):
  model = Event
  template_name = 'events/detail.html'

  def get_queryset(self):
    """
    Excludes any questions that aren't published yet.
    """
    return Event.objects.filter(start_time__lte=timezone.now())

class CategoryIndexView(generic.ListView):
  model = Category
  template_name = 'categories/index.html'
  context_object_name = 'categories_list'
  
  def get_queryset(self):
    ''' Get all categories.'''
    return Category.objects.all()

class CategoryDetailView(generic.DetailView):
  model = Category
  template_name = 'categories/detail.html'

'''
class ResultsView(generic.DetailView):
  model = Question
  template_name = 'polls/results.html'

#def index(request):
#  latest_question_list = Question.objects.order_by('-pub_date')[:5]
#  context = {'latest_question_list': latest_question_list}
#  return render(request, 'polls/index.html', context)
#
#def detail(request, question_id):
#  question = get_object_or_404(Question, pk=question_id)
#  return render(request, 'polls/detail.html', {'question': question})
#
#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    # Redisplay the question voting form.
    return render(request, 'polls/detail.html', {
        'question': question,
        'error_message': "You didn't select a choice.",
    })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', \
            args=(question.id,)))
'''
