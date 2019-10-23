import django_filters
from .models import Notes

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
