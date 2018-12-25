from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic 

from .models import Category, Event, Person, Relation, Rating
from .forms import EventForm

class IndexView(generic.ListView):
  template_name = 'main/index.html'
  context_object_name = 'main_page'

  def get_queryset(self):
    return None

class EventIndexView(generic.ListView):
  model = Event
  context_object_name = 'events_list'
  template_name = 'events/index.html'
  
  def get_queryset(self):
    ''' Excludes any events that haven't started yet. '''
    return Event.objects.filter(start_time__lte=timezone.now())

class EventDetailView(generic.DetailView):
  model = Event
  template_name = 'events/detail.html'
 
class EventCreateView(generic.CreateView):
  model = Event
  form_class = EventForm
  template_name = 'events/create.html'

  def form_valid(self, form):
    print(form.cleaned_data)
    return super().form_valid(form)

class EventUpdateView(generic.UpdateView):
  model = Event
  form_class = EventForm 
  template_name = 'events/update.html'

  def get_object(self, queryset=None):
    obj = Event.objects.get(pk=self.kwargs['pk'])
    return obj

  def form_valid(self, form):
    print(form.cleaned_data)
    return super().form_valid(form)

class EventDeleteView(generic.DeleteView):
  model = Event
  template_name = 'events/delete.html'

  def get_object(self, queryset=None):
    obj = Event.objects.get(pk=self.kwargs['pk'])
    return obj
  
  def get_success_url(self):
    return reverse('event_recorder:events-index')

class CategoryIndexView(generic.ListView):
  model = Category
  template_name = 'categories/index.html'
  context_object_name = 'categories_list'

class CategoryDetailView(generic.DetailView):
  model = Category
  template_name = 'categories/detail.html'

class PersonIndexView(generic.ListView):
  model = Person
  template_name = 'people/index.html'
  context_object_name = 'people_list'

class PersonDetailView(generic.DetailView):
  model = Person
  template_name = 'people/detail.html'

class RelationIndexView(generic.ListView):
  model = Relation
  template_name = 'relations/index.html'
  context_object_name = 'relations_list'

class RelationDetailView(generic.DetailView):
  model = Relation
  template_name = 'relations/detail.html'

class RatingIndexView(generic.ListView):
  model = Rating
  template_name = 'ratings/index.html'
  context_object_name = 'ratings_list'

class RatingDetailView(generic.DetailView):
  model = Rating
  template_name = 'ratings/detail.html'

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
