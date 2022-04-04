from django import forms 

class CreateNewList(forms.Form):
    name = forms.CharField(label = "UserName:", max_length= 17)
    check = forms.BooleanField
