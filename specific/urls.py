from specific.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('raji/',raji,name='raji'),
    path('mahi1/',mahi1,name='mahi1'),
]