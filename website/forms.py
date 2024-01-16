from django import forms

from .models import Logger, Booking

class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

"""SHIFT = (
    ("1", "Morning"),
    ("2", "Afernoon"),
    ("3", "Evening"),
)
class InputForm(forms.Form):
    first_name = forms.CharField(max_length= 200, required = False)
    last_name = forms.CharField(max_length=200, required=False)
    # shift = forms.ChoiceField(choices = SHIFT)
    time_log = forms.TimeField(help_text="Enter exact time")
    """