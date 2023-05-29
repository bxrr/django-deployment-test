from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), 
    path('about/', AboutPageView.as_view(), name='about')
    # general path arguments: directory, view object (http response), additional args (name='home') 
]