from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
from .forms import DonorSignUpForm
from .models import DonorInfo
import datetime
from datetime import timedelta

def reports(request):
    accounts = DonorInfo.objects.all()
    for account in accounts:
        created = account.date_created
        datecreated = created.strftime("%m-%d-%Y")
        name = account.name
        phone = account.phone
        email = account.email
        plusthirty = (created + datetime.timedelta(30))
        thirtydays = plusthirty.strftime("%m-%d-%Y")
        context = {'accounts': accounts, 'name':name, 'email':email, 'phone':phone, 'datecreated': datecreated,  'thirtydays': thirtydays}
        return render(request, 'reports.html', context)





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
            return HttpResponseRedirect('/donorform/')
    else:
        form = DonorSignUpForm()
    return render(request, 'signupform.html', {'form': form})


def donor_form(request):
    donor = DonorInfo.objects.latest('date_created')
    name = donor.name
    d = donor.date_created
    date = d.strftime("%m-%d-%Y")
    context = {'donor': donor, 'name': name, 'date': date}
    return render(request, 'donorform.html', context)
