from django import forms
from myapp.models import Person


class NameForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['first_name', 'last_name']