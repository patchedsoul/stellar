from .models import Notes, Goals, Tasks

def categories_processor(request):

	notes = Notes.objects.count()

	cgoals = Goals.objects.filter(complete=True).count()
	ngoals = Goals.objects.filter(complete=False).count()

	ctasks = Tasks.objects.filter(complete=True).count()
	ntasks = Tasks.objects.filter(complete=False).count()

	context = {
		'notes': notes,
		'cgoals': cgoals,
		'ngoals': ngoals,
		'ctasks': ctasks,
		'ntasks': ntasks
	}
	return context