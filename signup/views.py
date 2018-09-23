from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .forms import DonorSignUpForm, RecordForm
from .models import DonorInfo
import datetime
from datetime import timedelta
from django.shortcuts import render, HttpResponseRedirect, Http404, get_object_or_404

def record_recvd_dates(request):
    pk = DonorInfo.pk
    instance = DonorInfo.objects.get(pk=1)
    if request.method == "POST":
        form = RecordForm(request.POST, instance=instance)
    else:
        form = RecordForm(instance=instance)

def reports(request):
    accounts = DonorInfo.objects.all()
    for account in accounts:
        created = account.date_created
        payment_recvd = account.payment_recvd
        date_created = created.strftime("%m-%d-%Y")
        daterecvd = account.date_recvd
        date_recvd = daterecvd.strftime("%m-%d-%Y")
        name = account.name
        phone = account.phone
        email = account.email
        plusthirty = (created + datetime.timedelta(30))
        thirtydays = plusthirty.strftime("%m-%d-%Y")
        context = {'payment_recvd': payment_recvd, 'accounts': accounts, 'name':name, 'email':email, 'phone':phone, 'date_created': date_created,  'thirtydays': thirtydays}
        return render(request, 'reports.html', context)

def mailinglist(request):
    contacts = DonorInfo.objects.all()
    for contact in contacts:
        name = contact.name
        street_address = contact.street_address
        city = contact.city
        state = contact.state
        zipcode = contact.zipcode
        context = {'contacts': contacts, 'name': name, 'street_address': street_address, 'city':city, 'state': state, 'zipcode': zipcode}
        return render(request, 'mailinglist.html', context)




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
