from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.utils.text import slugify
from django.utils import timezone
from datetime import datetime

soar_situation_default = 'What problem/task/challenge are you trying to solve?'
soar_obstacles_default = 'What makes this problem/task/challenge difficult?'
soar_actions_default = 'What did you do to solve the problem/task/challenge and what skills did you use?'
soar_results_default = 'What were the results of your actions and how did it impact your program/team?'

class Notes(models.Model):
	title = models.CharField(max_length=100, blank=False)
	genre = models.CharField(max_length=20, blank=True)
	tag = models.CharField(max_length=20, blank=True)
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

class Soar(models.Model):
	date = models.DateField(default=timezone.now)
	genre = models.CharField(max_length=20, blank=True)
	tag = models.CharField(max_length=20, blank=True)
	slug = models.SlugField(max_length=150, unique=True, blank=True)
	situation = MarkdownxField(default=soar_situation_default)
	obstacle = MarkdownxField(default=soar_obstacles_default)
	action = MarkdownxField(default=soar_actions_default)
	result = MarkdownxField(default=soar_results_default)

	def __str__(self):
		return self.situation

	def s_formatted_markdown(self):
		return markdownify(self.situation)

	def o_formatted_markdown(self):
		return markdownify(self.obstacle)

	def a_formatted_markdown(self):
		return markdownify(self.action)

	def r_formatted_markdown(self):
		return markdownify(self.result)

	def _get_unique_slug(self):
		slug = slugify(self.situation)
		unique_slug = slug
		num = 1
		while Soar.objects.filter(slug=unique_slug).exists():
			unique_slug = '{}-{}'.format(slug, num)
			num += 1
		return unique_slug

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = self._get_unique_slug()
		super().save(*args, **kwargs)


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
