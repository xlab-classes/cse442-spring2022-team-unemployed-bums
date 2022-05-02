from django import forms

daychoices = [('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10'),('11', '11'),('12', '12'),('13', '13'),('14', '14'),('15', '15'),('16', '16'),('17', '17'),('18', '18'),('19', '19'),('20', '20'),('21', '21'),('22', '22'),('23', '23'),('24', '24'),('25', '25'),('26', '26'),('27', '27'),('28', '28'),('29', '29'),('30', '30'),('31', '31')]
monthchoices = [('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10'),('11', '11'),('12', '12')]
yearchoices = [('2022', '2022'),('2023', '2023'),('2024', '2024')]
recurringchoices = [("no", "No"), ("weekly", "Weekly"), ("monthly", "Monthly"), ("yearly", "Yearly")]

class CreateNewListing(forms.Form):
    title = forms.CharField(max_length=200, label="Title")
    description = forms.CharField(widget=forms.Textarea, label="Description")
    eventday = forms.IntegerField(widget=forms.Select(choices=daychoices))
    eventmonth = forms.IntegerField(widget=forms.Select(choices=monthchoices))
    eventyear = forms.IntegerField(widget=forms.Select(choices=yearchoices))
    recurring = forms.CharField(widget=forms.Select(choices=recurringchoices), required=False)
    outdoors = forms.BooleanField(label="Outdoors", required=False)
    recreation = forms.BooleanField(label="Recreation", required=False)
    sports = forms.BooleanField(label="Sports", required=False)
    learning = forms.BooleanField(label="Learning", required=False)