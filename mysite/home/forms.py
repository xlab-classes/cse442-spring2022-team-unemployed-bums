from django import forms

sortOptions = [("newest", "Newest"), ("mostpopular", "Most Popular"), ("leastpopular", "Least Popular")]

class Tagsform(forms.Form):
    outdoors = forms.BooleanField(label="Outdoors", required=False)
    recreation = forms.BooleanField(label="Recreation", required=False)
    sports = forms.BooleanField(label="Sports", required=False)
    learning = forms.BooleanField(label="Learning", required=False)
    sortOption = forms.CharField(label="Sorting", required=False, widget=forms.Select(choices=sortOptions))