from django import forms
from .models import Route

class RouteForm(forms.ModelForm):
    """
    A ModelForm for creating and updating Route instances.
    Includes fields for source, destination, position, and duration.
    """
    class Meta:
        model = Route
        fields = ['source', 'destination', 'position', 'duration']

class SearchForm(forms.Form):
    """
    Form for searching flights by airport code, number of steps, and direction.
    """
    airport_code = forms.CharField(max_length=10)
    steps = forms.IntegerField()
    direction = forms.ChoiceField(choices=[('left', 'Left'), ('right', 'Right')])
