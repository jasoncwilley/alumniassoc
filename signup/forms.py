from .models import DonorInfo
from django import forms
import datetime
class DonorSignUpForm(forms.Form):
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
