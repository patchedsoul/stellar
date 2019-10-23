from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.utils.text import slugify
from django.utils import timezone
from datetime import datetime



class Notes(models.Model):
	title = models.CharField(max_length=100, blank=False)
	genre = models.CharField(max_length=20, blank=False)
	tag = models.CharField(max_length=20, blank=False, default='none')
	body = MarkdownxField()
	date = models.DateField(default=timezone.now)
	slug = models.SlugField(max_length=150, unique=True, blank=True)

	def __str__(self):
		return self.title

	def formatted_markdown(self):
		return markdownify(self.body)

	def _get_unique_slug(self):
		slug = slugify(self.title)
		unique_slug = slug
		num = 1
		while Notes.objects.filter(slug=unique_slug).exists():
		    unique_slug = '{}-{}'.format(slug, num)
		    num += 1
		return unique_slug

	def save(self, *args, **kwargs):
		if not self.slug:
		    self.slug = self._get_unique_slug()
		super().save(*args, **kwargs)

	class Meta:
		verbose_name_plural = "Notes"

class Goals(models.Model):
	tag = models.CharField(max_length=100, default='goals', blank=False)
	complete = models.BooleanField(default=False, blank=False)
	body = MarkdownxField()
	end_date = models.DateField(default=timezone.now)
	def formatted_markdown(self):
		return markdownify(self.body)
	def time_left(self):
		end = datetime.combine(self.end_date, datetime.min.time())
		now = datetime.combine(datetime.now(), datetime.min.time())
		return (end - now).days
	class Meta:
		verbose_name_plural = "Goals"

class Tasks(models.Model):
	tag = models.CharField(max_length=100, default='tasks', blank=False)
	complete = models.BooleanField(default=False, blank=False)
	body = MarkdownxField()
	end_date = models.DateField(default=timezone.now)
	def time_left(self):
		end = datetime.combine(self.end_date, datetime.min.time())
		now = datetime.combine(datetime.now(), datetime.min.time())
		return (end - now).days
	def formatted_markdown(self):
		return markdownify(self.body)
	class Meta:
		verbose_name_plural = "Tasks"
