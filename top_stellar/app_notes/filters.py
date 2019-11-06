import django_filters
from .models import Notes, Soar, Goals, Tasks

choices = (
    (True, "YES"),
    (False, "NO")
)

class NotesFilter(django_filters.FilterSet):
	title = django_filters.CharFilter(field_name='title', lookup_expr='iexact', label='Title')
	genre = django_filters.CharFilter(field_name='genre', lookup_expr='iexact', label='Genre')
	tag = django_filters.CharFilter(field_name='tag', lookup_expr='iexact', label='Tag')
	body = django_filters.CharFilter(field_name='body', lookup_expr='icontains', label='Content')
	m_date = django_filters.NumberFilter(field_name='date', lookup_expr='month', label='Month (mm)')
	y_date = django_filters.NumberFilter(field_name='date', lookup_expr='year', label='Year (yyyy)')

	class Meta:
		model = Notes
		fields = ['title', 'genre', 'tag', 'body', 'm_date', 'y_date']

	def __init__(self, *args, **kwargs):
		super(NotesFilter, self).__init__(*args, **kwargs)
		if self.data == {}:
			self.queryset = self.queryset.none()

class SoarFilter(django_filters.FilterSet):
	m_date = django_filters.NumberFilter(field_name='date', lookup_expr='month', label='Month (mm)')
	y_date = django_filters.NumberFilter(field_name='date', lookup_expr='year', label='Year (yyyy)')
	genre = django_filters.CharFilter(field_name='genre', lookup_expr='iexact', label='Genre')
	tag = django_filters.CharFilter(field_name='tag', lookup_expr='iexact', label='Tag')
	s_body = django_filters.CharFilter(field_name='situation', lookup_expr='icontains', label='Situation')
	o_body = django_filters.CharFilter(field_name='obstacle', lookup_expr='icontains', label='Obstacle')
	a_body = django_filters.CharFilter(field_name='action', lookup_expr='icontains', label='Action')
	r_body = django_filters.CharFilter(field_name='result', lookup_expr='icontains', label='Result')

	class Meta:
		model = Soar
		fields = ['m_date', 'y_date', 'genre', 'tag', 's_body', 'o_body', 'a_body', 'r_body']

	def __init__(self, *args, **kwargs):
		super(SoarFilter, self).__init__(*args, **kwargs)
		if self.data == {}:
			self.queryset = self.queryset.none()

class GoalsFilter(django_filters.FilterSet):
	tag = django_filters.CharFilter(field_name='tag', lookup_expr='iexact', label='Tag')
	body = django_filters.CharFilter(field_name='body', lookup_expr='icontains', label='Content')
	m_date = django_filters.NumberFilter(field_name='end_date', lookup_expr='month', label='Month (mm)')
	y_date = django_filters.NumberFilter(field_name='end_date', lookup_expr='year', label='Year (yyyy)')
	complete = django_filters.BooleanFilter(field_name='complete')

	class Meta:
		model = Goals
		fields = ['tag', 'body', 'm_date', 'y_date', 'complete']

	def __init__(self, *args, **kwargs):
		super(GoalsFilter, self).__init__(*args, **kwargs)
		if self.data == {}:
			self.queryset = self.queryset.none()

class TasksFilter(django_filters.FilterSet):
	tag = django_filters.CharFilter(field_name='tag', lookup_expr='iexact', label='Tag')
	body = django_filters.CharFilter(field_name='body', lookup_expr='icontains', label='Content')
	m_date = django_filters.NumberFilter(field_name='end_date', lookup_expr='month', label='Month (mm)')
	y_date = django_filters.NumberFilter(field_name='end_date', lookup_expr='year', label='Year (yyyy)')
	complete = django_filters.BooleanFilter(field_name='complete')

	class Meta:
		model = Tasks
		fields = ['tag', 'body', 'm_date', 'y_date', 'complete']

	def __init__(self, *args, **kwargs):
		super(TasksFilter, self).__init__(*args, **kwargs)
		if self.data == {}:
			self.queryset = self.queryset.none()