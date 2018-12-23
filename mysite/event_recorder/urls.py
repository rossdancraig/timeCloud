from django.urls import path
from . import views

app_name = 'event_recorder'
urlpatterns = [
#  path('', views.IndexView.as_view(), name='index'),
  path('', views.IndexView.as_view(), name='index'),
  path('events/', views.EventIndexView.as_view(), name='events-index'),
  path('events/<int:pk>/', views.EventDetailView.as_view(), 
        name='event-detail'),
  path('categories/', views.CategoryIndexView.as_view(),
        name='categories-index'),
  path('categories/<int:pk>/', views.CategoryDetailView.as_view(), 
        name='category-detail'),
  path('people/', views.PersonIndexView.as_view(),
        name='people-index'),
  path('people/<int:pk>/', views.PersonDetailView.as_view(), 
        name='person-detail'),
  path('relations/', views.RelationIndexView.as_view(),
        name='relations-index'),
  path('relations/<int:pk>/', views.RelationDetailView.as_view(), 
        name='relation-detail'),
#  path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#  path('<int:question_id>/vote/', views.vote, name='vote'),
]
