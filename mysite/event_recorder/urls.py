from django.urls import path
from . import views

app_name = 'event_recorder'
urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),

  path('events/', views.EventIndexView.as_view(), 
        name='events-index'),
  path('events/<int:pk>/', views.EventDetailView.as_view(), 
        name='event-detail'),
  path('events/create/', views.EventCreateView.as_view(), 
        name='event-create'),
  path('events/<int:pk>/update/', views.EventUpdateView.as_view(), 
        name='event-update'),
  path('events/<int:pk>/delete/', views.EventDeleteView.as_view(), 
        name='event-delete'),

  path('categories/', views.CategoryIndexView.as_view(),
        name='categories-index'),
  path('categories/<int:pk>/', views.CategoryDetailView.as_view(), 
        name='category-detail'),
  path('categories/create/', views.CategoryCreateView.as_view(), 
        name='category-create'),
  path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), 
        name='category-update'),
  path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), 
        name='category-delete'),


  path('people/', views.PersonIndexView.as_view(),
        name='people-index'),
  path('people/<int:pk>/', views.PersonDetailView.as_view(), 
        name='person-detail'),
  path('relations/', views.RelationIndexView.as_view(),
        name='relations-index'),
  path('relations/<int:pk>/', views.RelationDetailView.as_view(), 
        name='relation-detail'),
  path('ratings/', views.RatingIndexView.as_view(),
        name='ratings-index'),
  path('ratings/<int:pk>/', views.RatingDetailView.as_view(), 
        name='ratings-detail'),
]
