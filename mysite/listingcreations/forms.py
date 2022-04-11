from django import forms

tagoptions = [('outdoors', "Outdoors"), ("recreation", "Recreation"), ("sports", "Sports"), ("learning", "Learning")]

class CreateNewListing(forms.Form):
    title = forms.CharField(max_length=200, label="Title")
    description = forms.CharField(widget=forms.Textarea, label="Description")
    outdoors = forms.BooleanField(label="Outdoors", required=False)
    recreation = forms.BooleanField(label="Recreation", required=False)
    sports = forms.BooleanField(label="Sports", required=False)
    learning = forms.BooleanField(label="Learning", required=False)