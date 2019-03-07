from django.conf.urls import url
from alertasApp import views

urlpatterns= [
    url(r'^$',views.index, name='index'),
]
