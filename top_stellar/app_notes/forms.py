from django import forms
from .models import Notes, Goals, Tasks

class NotesForm(forms.ModelForm):
	class Meta:
		model = Notes
		fields = ['title', 'genre', 'tag', 'body', 'date']

class GoalsForm(forms.ModelForm):
	class Meta:
		model = Goals
		fields = ['tag', 'complete', 'body', 'end_date']

class TasksForm(forms.ModelForm):
	class Meta:
		model = Tasks
		fields = ['tag', 'complete', 'body', 'end_date']