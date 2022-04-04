from django.db import models

search_tag_choices = ['Outdoors', 'sports', 'recreational', 'edjucational']

class Snippet(models.model):
    title = models.CharField()
    description = models.CharField(widget=models.Textarea)
    searchTags = models.MultipleChoiceField(required=False, widget=models.CheckboxSelectMultiple,
                                           choices=search_tag_choices)

