from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    url('index/',barrowed_index,name='index'),
    url(r'^(?P<id>\d+)/delete/$', return_barrow, name='return'),


]