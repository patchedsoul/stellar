from django.urls import path, re_path
from app_notes import views
from .models import Notes, Soar, Goals, Tasks
from .filters import NotesFilter, SoarFilter, GoalsFilter, TasksFilter
from django_filters.views import FilterView

app_name = 'app_notes'

urlpatterns = [
	path('', views.HomeListView.as_view(), name='homelist'),
	
	re_path(r'^taglist/(?P<notes_tag>.*)/$', views.HomeTagsListView.as_view(), name="taglist"),
	re_path(r'^genrelist/(?P<notes_genre>.*)/$', views.HomeGenreListView.as_view(), name="genrelist"),

	re_path(r'^staglist/(?P<soar_tag>.*)/$', views.HomeSoarTagsListView.as_view(), name="staglist"),
	re_path(r'^sgenrelist/(?P<soar_genre>.*)/$', views.HomeSoarGenreListView.as_view(), name="sgenrelist"),

	path('search/', views.SearchListView.as_view(), name='searcher'),
	path('ssearch/', views.SoarSearchListView.as_view(), name='ssearcher'),
    path('gsearch/', views.GoalsSearchListView.as_view(), name='gsearcher'),
    path('tsearch/', views.TasksSearchListView.as_view(), name='tsearcher'),
	path('create/', views.NotesCreateView.as_view(), name='creater'),
	path('screate/', views.SoarCreateView.as_view(), name='screater'),
	path('gcreate/', views.GoalsCreateView.as_view(), name='gcreater'),
	path('tcreate/', views.TasksCreateView.as_view(), name='tcreater')
]