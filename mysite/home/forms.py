from django import forms

class Tagsform(forms.Form):
    outdoors = forms.BooleanField(label="Outdoors", required=False)
    recreation = forms.BooleanField(label="Recreation", required=False)
    sports = forms.BooleanField(label="Sports", required=False)
    learning = forms.BooleanField(label="Learning", required=False)