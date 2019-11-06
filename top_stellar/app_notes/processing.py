from .models import Notes, Soar, Goals, Tasks
from django.db.models import Count
from collections import Counter

TOP = 20

def return_top_tags(model_name, attribute_name, is_nulls):

    # Create a list from a query
    top_tags = []
    if model_name == 'notes':
        top_tags = list(Notes.objects.values_list(attribute_name, flat=True))
    elif model_name == 'soar':
        top_tags = list(Soar.objects.values_list(attribute_name, flat=True))
    elif model_name == 'goals':
        top_tags = list(Goals.objects.values_list(attribute_name, flat=True))
    elif model_name == 'tasks':
        top_tags = list(Tasks.objects.values_list(attribute_name, flat=True))

    # Sort the list from most popular to least popular
    top_tags = [item for items, c in Counter(top_tags).most_common() for item in [items] * c]

    # Remove duplicate tags in the list
    seen = set()
    top_tags = [x for x in top_tags if not (x in seen or seen.add(x))]

    # Remove nulls should the attributes option "blank" be set to true
    if is_nulls == True:
        top_tags = [x for x in top_tags if x]

    # Return only the top X number of tags defined by variable TOP
    short_by = TOP - len(top_tags)
    if short_by < TOP:
        return top_tags
    else:
        return top_tags[:TOP]


def return_num_occur(model_name, top_tags, attr_name):
    occur = [0] * len(top_tags)

    if model_name == 'notes':
        for x, label in enumerate(top_tags):
            if attr_name == 'tag':
                occur[x] = Notes.objects.filter(tag__exact=top_tags[x]).count()
            elif attr_name == 'genre':
                occur[x] = Notes.objects.filter(genre__exact=top_tags[x]).count()
    elif model_name == 'soar':
        for x, label in enumerate(top_tags):
            if attr_name == 'tag':
                occur[x] = Soar.objects.filter(tag__exact=top_tags[x]).count()
            elif attr_name == 'genre':
                occur[x] = Soar.objects.filter(genre__exact=top_tags[x]).count()
    elif model_name == 'goals':
        for x, label in enumerate(top_tags):
            if attr_name == 'tag':
                occur[x] = Goals.objects.filter(tag__exact=top_tags[x]).count()
            else:
                occur[x] = 0
    elif model_name == 'tasks':
        for x, label in enumerate(top_tags):
            if attr_name == 'tag':
                occur[x] = Tasks.objects.filter(tag__exact=top_tags[x]).count()
            else:
                occur[x] = 0

    return occur