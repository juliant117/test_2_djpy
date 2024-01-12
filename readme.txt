#project test_2 
it is a project to trie to create a web wit django and trie to deploy it in google cloud

#----------------- django -----------------------------------

#----------------- django -----------------------------------

#----------------- django -----------------------------------
#create virtual env
#python3 -m venv venv   #this have problems with some libraries
virtualenv venv
#activate virtual env
./venv/Scripts/activate
#check the libraries installed
python manage.py runserver
pip freeze
#install django
pip install django
#----------------- django -----------------------------------
#start django
django-admin startproject TEST_2 .   #django-admin startproject "name of project " "laction of project"
#----------------- django -----------------------------------
#create other app
python manage.py startapp schedule   #python manage.py startapp "name of the app"
python manage.py makemigrations schedule   #python manage.py makemigrations "name of app"
python manage.py migrate
#add the app to sttings
->sttings.py
->INSTALLED_APPS
#add url.py to the app folder



#--------------------- python manage.py shell -------------------------------

from polls.models import Choice, Question
Question.objects.all()          see the questions
from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())        create a question
q.save()
q.id
q.question_text
q.pub_date
q.question_text = "What's up?"
q.save()
Question.objects.all()


#--------------------- super -------------------------------
python manage.py createsuperuser

admin25
julianthole117@gmail.com
diablo125

#--------------------- tests -------------------------------

$ python manage.py shell

>>> import datetime
>>> from django.utils import timezone
>>> from polls.models import Question
>>> # create a Question instance with pub_date 30 days in the future
>>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
>>> # was it published recently?
>>> future_question.was_published_recently()
True

#create test

#run
python manage.py test schedule

