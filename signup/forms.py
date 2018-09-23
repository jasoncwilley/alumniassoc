from .models import DonorInfo
from django import forms
import datetime
from bootstrap_datepicker.widgets import DatePicker

class DonorSignUpForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'placehoder' : 'Example: Francis Willey'}))
    street_address = forms.CharField(max_length=35)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=2)
    zipcode = forms.CharField(max_length=5)
    email = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=35)
    date_created = forms.DateTimeField(
        widget=forms.HiddenInput(),
        required=False
    )

    class Meta:
       model = DonorInfo
       fields = ['name', 'street_address', 'city', 'state', 'zipcode', 'email', 'phone']
       excluded = ['date_created']

class RecordForm(forms.Form):
    name = forms.ModelChoiceField(queryset=DonorInfo.objects.all().order_by('name'))
    date = forms.DateField(
        widget=DatePicker(
            options={
                "format": "mm/dd/yyyy",
                "autoclose": True
            }
        )
    )
    payment_recvd = forms.BooleanField(required=False)
    def clean_recvd_date(self):
        data = self.cleaned_data['payment_recvd']
        if data > datetime.date.today():
            raise ValidationError(_('Date Cannot Be in the Future'))

            return data


    class Meta:
        model = DonorInfo
        fields = ['name', 'payment_recvd', 'date_recvd', 'street_address', 'city', 'state', 'zipcode', 'email', 'phone' ]
