"""mailinglist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from signup.views import index
from signup import views

app_name='signup'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', include('signup.urls')),
    path('', views.index, name='index'),
    path('signupform/', views.sign_up_form, name='signupform'),
    path('donorform/', views.donor_form, name='donorform'),
    path('reports/', views.reports, name='reports'),
    path('mailinglist/', views.mailinglist, name='mailinglist'),
    path('updates/', views.record_recvd_dates, name='updates'),
    path('updates/<pk>/recvd/', views.record_recvd_dates, name='recvddate'),
    path('latepayments/', views.latepayments, name='latepayments'),
    path('makeadonation/', views.makeadonation, name='makeadonation')

    ]
