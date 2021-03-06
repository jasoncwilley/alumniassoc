from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .forms import DonorSignUpForm, RecordForm
from .models import DonorInfo
import datetime
from datetime import timedelta
from django.shortcuts import render, HttpResponseRedirect, Http404, get_object_or_404
from datetime import datetime, timedelta
from datetime import timedelta

def september(request):
    payments = DonorInfo.objects.all()
    name = payments.name
    date_recvd = payments.date_recvd
    amount_recvd = payments.amount_recvd
    d1 = datetime(2018, 9, 1)
    d2 = datetime(2018, 9, 30)
    sept = DonorInfo.objects.filter(date_recvd__gte=d1, date_recvd__lte=d2)

    for x in sept:
        t = x.amount_recvd
        tlist=[]
        for x in sept:
            tlist.append(x.amount_recvd)
            sept = (sum(tlist))
    context = { 'paytments': payments, 'sept':sept, 'amount_recvd':amount_recvd, 'name':name}
    return render(request, 'jan.html', context)
    

def october(request):
    pass

def november(request):
    pass


def latepayments(request):
    accounts = DonorInfo.objects.all()
    last_month = datetime.today() - timedelta(days=30)
    lateaccounts = DonorInfo.objects.all().filter(date_created__lte=last_month).filter(**{'payment_recvd': 'None'})
    for account in accounts:
        created = account.date_created
        plusthirty = created + timedelta(30)
        thirtydays = plusthirty

        context = { 'lateaccounts': lateaccounts, 'accounts':accounts, 'thirtydays': thirtydays }
        return render(request, 'latepayments.html', context)

def record_recvd_dates(request):
    pk = DonorInfo.pk
    instance = DonorInfo.objects.get(pk=1)
    if request.method == "POST":
        form = RecordForm(request.POST, instance=instance)
    else:
        form = RecordForm(instance=instance)


def totals(request):
    accounts = DonorInfo.objects.all()
    for account in accounts:
        created = account.date_created
        payment_recvd = account.payment_recvd
        date_created = created.strftime("%m-%d-%Y")
        date_recvd = account.date_recvd
        name = account.name
        phone = account.phone
        email = account.email
        plusthirty = (created + timedelta(30))
        thirtydays = plusthirty.strftime("%m-%d-%Y")
        context = {'payment_recvd': payment_recvd, 'accounts': accounts, 'name':name, 'email':email, 'phone':phone, 'date_created': date_created,  'thirtydays': thirtydays}
        return render(request, '41369.html', context)





def reports(request):
    accounts = DonorInfo.objects.all()
    for account in accounts:
        created = account.date_created
        payment_recvd = account.payment_recvd
        date_created = created.strftime("%m-%d-%Y")
        date_recvd = account.date_recvd
        name = account.name
        phone = account.phone
        email = account.email
        plusthirty = (created + timedelta(30))
        thirtydays = plusthirty.strftime("%m-%d-%Y")
        context = {'payment_recvd': payment_recvd, 'accounts': accounts, 'name':name, 'email':email, 'phone':phone, 'date_created': date_created,  'thirtydays': thirtydays}
        return render(request, '41369.html', context)

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

def makeadonation(request):
    return render( request, 'makeadonation.html')
