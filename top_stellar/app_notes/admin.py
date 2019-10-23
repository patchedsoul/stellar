from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Notes, Goals, Tasks

class NotesAdmin(MarkdownxModelAdmin):
	list_display = ('title', 'genre', 'date', 'tag')
class GoalsAdmin(MarkdownxModelAdmin):
	list_display = ('tag', 'end_date', 'complete')
class TasksAdmin(MarkdownxModelAdmin):
	list_display = ('tag', 'end_date', 'complete')


admin.site.register(Notes, NotesAdmin)
admin.site.register(Goals, GoalsAdmin)
admin.site.register(Tasks, TasksAdmin)