from django.urls import path
from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^home/', hellow, name='hello'),
    url(r'^friend/$', friend, name='friend'),
    url(r'^data/$', data_from_db, name="it will fetch data from db"),
    url(r'^forms/$',forms),
    url(r'^RegSuccessful/$',RegSuccessful),
    url(r'^registration/$', registration),
    url(r'^login/$',user_login, name="login"),
    url(r'^success/$', success),
    url(r'^logout/$', logout),
    #url(r'^Home/$', home, name="Home page of app"),


]