from django.urls import path
from . import views

app_name = 'event_recorder'
urlpatterns = [
#  path('', views.IndexView.as_view(), name='index'),
  path('', views.IndexView.as_view(), name='index'),
  path('events/', views.EventIndexView, name='events-index'),
  path('events/<int:pk>/', views.EventDetailView.as_view(), 
        name='event-detail'),
  path('categories/', views.CategoryIndexView,
        name='categories-index'),
  path('categories/<int:pk>/', views.CategoryDetailView.as_view(), 
        name='category-detail'),
#  path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#  path('<int:question_id>/vote/', views.vote, name='vote'),
]
