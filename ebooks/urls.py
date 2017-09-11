"""

"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^ebooks$', views.book_details, name='book_details'),
    url(r'^([0-9]+)/$', views.book_details, name='book_details'),

]
