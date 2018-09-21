from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
from .forms import DonorSignUpForm
from .models import DonorInfo
def index(request):
    return render(request, 'signup/index.html')

def sign_up_form(request):
    if request.method =='POST':
        form = DonorSignUpForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.name = form.cleaned_data['name']
            new.street_address = form.cleaned_data['street_address']
            new.city = form.cleaned_data['city']
            new.state = form.cleaned_data['state']
            new.zipcode = form.cleaned_data['zipcode']
            new.email = form.cleaned_data['email']
            new.phone = form.cleaned_data['phone']
            new.save()
            return HttpResponseRedirect('/signupform/')
    else:
        form = DonorSignUpForm()
    return render(request, 'signupform.html', {'form': form})
