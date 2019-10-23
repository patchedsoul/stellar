from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView
from .models import Notes, Goals, Tasks
from .filters import NotesFilter
from .forms import NotesForm, GoalsForm, TasksForm
from django_filters.views import FilterView
import app_notes.processing as proc
from django.urls import reverse_lazy

#--------------------------------------------------------------------------------

class HomeListView(ListView):
	template_name = 'app_notes/app_notes.html'
	model = Notes

	def get_queryset(self):
		return Notes.objects.order_by('-date')

	def get_context_data(self, **kwargs):
		t_x = proc.return_top_tags('notes', 'tag', False)
		t_y = proc.return_num_occur('notes', t_x, 'tag')

		g_x = proc.return_top_tags('notes', 'genre', False)
		g_y = proc.return_num_occur('notes', g_x, 'genre')

		context = super().get_context_data(**kwargs)
		context['tags_list'] = t_x
		context['genres_list'] = g_x

		context['incomplete_goals'] = Goals.objects.filter(complete=False)
		context['incomplete_tasks'] = Tasks.objects.filter(complete=False)

		context['tag_data'] = zip(t_x, t_y)
		context['genre_data'] = zip(g_x, g_y)
		
		return context

#--------------------------------------------------------------------------------

class HomeTagsListView(ListView):
	template_name = 'app_notes/app_notes_tag_list.html'
	model = Notes
	paginate_by = 10

	def get_queryset(self):
		return Notes.objects.filter(tag__icontains=self.kwargs['notes_tag']).order_by('-date')

#--------------------------------------------------------------------------------

class HomeGenreListView(ListView):
	template_name = 'app_notes/app_notes_genre_list.html'
	model = Notes
	paginate_by = 10
	def get_queryset(self):
		return Notes.objects.filter(genre__icontains=self.kwargs['notes_genre']).order_by('-date')

#--------------------------------------------------------------------------------

class FilterListView(ListView):
	filterset_class = None
	def get_queryset(self):
		queryset = super().get_queryset().order_by('-date')
		self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
		return self.filterset.qs.distinct()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = self.filterset
		return context

class SearchListView(FilterListView):
	model = Notes
	filterset_class = NotesFilter
	template_name = 'app_notes/app_notes_search.html'

#--------------------------------------------------------------------------------

class NotesCreateView(CreateView):
	template_name = 'app_notes/app_notes_create.html'
	form_class = NotesForm
	model = Notes
	success_url = reverse_lazy('app_notes:homelist')

#--------------------------------------------------------------------------------

class GoalsCreateView(CreateView):
	template_name = 'app_notes/goals.html'
	form_class = GoalsForm
	model = Goals
	success_url = reverse_lazy('app_notes:homelist')

#--------------------------------------------------------------------------------

class TasksCreateView(CreateView):
	template_name = 'app_notes/tasks.html'
	form_class = TasksForm
	model = Tasks
	success_url = reverse_lazy('app_notes:homelist')