from django import forms
from .models import Snippet
from crispy_forms.helper import FormHelper


#def contact(request):
#    return HttpResponse('contact view')

search_tag_choices = ['Outdoors', 'sports', 'recreational', 'edjucational']

class ListingForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    searchTags = forms.MultipleChoiceField(required = False, widget=forms.CheckboxSelectMultiple, choices = search_tag_choices)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper


class SnippetForm(forms.ModelForm):

    class Mets:
        model = Snippet
        fields = ('title', 'description', 'searchTags')