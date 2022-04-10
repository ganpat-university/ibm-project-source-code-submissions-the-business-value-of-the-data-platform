from django.forms import ModelForm, DateInput
from .models import NewComplaints

class DateInput(DateInput):
    input_type = 'date'

class NewComplaintsForm(ModelForm):
    class Meta:
        model = NewComplaints
        fields = '__all__'
        widgets = {
            'dateReceived': DateInput()
        }