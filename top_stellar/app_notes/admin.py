from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Notes, Soar, Goals, Tasks

class NotesAdmin(MarkdownxModelAdmin):
	list_display = ('title', 'genre', 'date', 'tag')
class SoarAdmin(MarkdownxModelAdmin):
    list_display = ('situation', 'genre', 'tag', 'date')
class GoalsAdmin(MarkdownxModelAdmin):
	list_display = ('tag', 'end_date', 'complete')
class TasksAdmin(MarkdownxModelAdmin):
	list_display = ('tag', 'end_date', 'complete')


admin.site.register(Notes, NotesAdmin)
admin.site.register(Soar, SoarAdmin)
admin.site.register(Goals, GoalsAdmin)
admin.site.register(Tasks, TasksAdmin)