from django.urls import path
from . import views

urlpatterns=[
    path('cnt/',views.contact,name='contact')
]