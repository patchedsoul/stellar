from django.urls import path, re_path
from app_notes import views
from .models import Notes
from .filters import NotesFilter
from django_filters.views import FilterView

app_name = 'app_notes'

urlpatterns = [
	path('', views.HomeListView.as_view(), name='homelist'),
	re_path(r'^taglist/(?P<notes_tag>.*)/$', views.HomeTagsListView.as_view(), 
		name="taglist"),
	re_path(r'^genrelist/(?P<notes_genre>.*)/$', views.HomeGenreListView.as_view(), 
		name="genrelist"),
	path('search/', views.SearchListView.as_view(), name='searcher'),
	path('create/', views.NotesCreateView.as_view(), name='creater'),
	path('gcreate/', views.GoalsCreateView.as_view(), name='gcreater'),
	path('tcreate/', views.TasksCreateView.as_view(), name='tcreater')
]