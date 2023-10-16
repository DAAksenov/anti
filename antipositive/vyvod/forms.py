from django import forms

class StudentForm(forms.Form):
    uuid = forms.CharField(label="your uuid",max_length=50)
