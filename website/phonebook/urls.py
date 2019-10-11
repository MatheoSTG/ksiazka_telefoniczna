from django.urls import re_path
from . import views

app_name = 'phonebook'

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^search/(?P<data>.*)$', views.SearchView.as_view(), name='search'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='person_detail'),
    re_path(r'^person/add/$', views.PersonCreate.as_view(), name='add_person'),
    re_path(r'^person/(?P<pk>[0-9]+)/$', views.PersonUpdate.as_view(), name='update_person'),
    re_path(r'^person/(?P<pk>[0-9]+)/delete/$', views.PersonDelete.as_view(), name='delete_person'),
    re_path(r'^(?P<pk>[0-9]+)/addphone/$', views.PhoneCreate.as_view(), name='add_phone'),
    re_path(r'^phone/(?P<pk>[0-9]+)/(?P<pk2>[0-9]+)/$', views.PhoneUpdate.as_view(), name='update_phone'),
    re_path(r'^phone/(?P<pk>[0-9]+)/(?P<pk2>[0-9]+)/delete/$', views.PhoneDelete.as_view(), name='delete_phone'),
    re_path(r'^(?P<pk>[0-9]+)/addemail/$', views.EmailCreate.as_view(), name='add_email'),
    re_path(r'^email/(?P<pk>[0-9]+)/(?P<pk2>[0-9]+)/$', views.EmailUpdate.as_view(), name='update_email'),
    re_path(r'^email/(?P<pk>[0-9]+)/(?P<pk2>[0-9]+)/delete/$', views.EmailDelete.as_view(), name='delete_email'),
]

