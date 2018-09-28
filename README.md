# Saint Leo School Alumni Association Donation Page

![N|Solid](http://oi66.tinypic.com/b7m246.jpg) 


Simple webpage I created for the St. Leo School Alumni Association.  Features include a donor donor date base, mailing list, severar reports to track donations and identify members accounts who are overdue.  Majority of the code used is Python but the reports utilize some basic JavaScript to enhance thier functionality.  Feel free to clone and modify to suite your needs!  If you would like ot try it before you clone check out the most recent version at https://stleos.heroduapp.com

### Getting Started
###### Below is a list of the required software needed to ensure proper functioning of the application.
# 
dj-database-url==0.5.0
Django==2.0.8
django-bootstrap==0.2.4
django-bootstrap-datepicker==1.3
django-bootstrap-form==3.4
django-bootstrap3==11.0.0
django-heroku==0.3.1
django-widget-tweaks==1.4.3
gunicorn==19.9.0
psycopg2==2.7.5
psycopg2-binary==2.7.5
pytz==2018.5


### Installation
In order to get up and running please follow the folloing instructions.  If you have done this sort of thing before installation simply create a virtual enviornment, clone the repo and pip install on the requirements.txt file before firing up Django.  If this is your first time or you are new to Django follow the steps below to install the application.   

First you will need to clone the github repository which will download the software to your machine
```sh
$ git clone https://github.com/jasoncwilley/alunniassoc.git
```
Once the software finishes downloading you should create virtual enviroment to run the software in using following command.  
```sh
$ mkvirtualenv alumniassoc
```

Now fire up the virtual environment
```sh
$ workon alumniassoc
```
If all went well your command prompt should change from
```sh
$ 
```
to 
```sh
(alumniassoc) $
```
Now that the vm is running cd into the Chatango directory
```sh
(alumniassoc) $ cd alumniassoc
```
Install the the remaining dependencies by running the following command 
```sh
(alumniassoc) $ pip install -r requirements.txt
```
Before you can use Chatango you need migrate the create/migrate the database
```sh
(alumniassoc) $ python manage.py makemigrations
```
then update the database with 
```sh
(alumniassoc) $ python manage.py migrate
```
You should be good to go if you made it this far and you can start Chatango with the following command
```sh
(alumniassoc) $ python manage.py runserver 0.0.0.0:5555
```
Now open up a web browser and navigate to 0.0.0.0:5555 and you should see the homepage page.  

The reporting section does not have links on the home page per the SLAA request.  To view the reporting secition direct your browser to 0.0.0.0:5555/reports.html

