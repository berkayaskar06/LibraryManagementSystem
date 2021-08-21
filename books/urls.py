from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    url('index/',books_index,name='index'),
    url(r'^(?P<id>\d+)/$',books_details,name='detail'),
    url('create/',books_create,name='create'),
    url(r'^(?P<id>\d+)/update$',books_update,name='update'),
    url(r'^(?P<id>\d+)/delete/$',books_delete,name='delete'),
    # url(r'^(?P<id>\d+)/$', books_barrow, name='barrow'),

]