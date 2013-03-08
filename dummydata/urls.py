from django.conf.urls import patterns, url
from dummydata import views as dummydata

urlpatterns = patterns('',
    url(r'contact/generate/$', dummydata.GenerateContacts.as_view(),
        name='generate-contacts'),
    url(r'connection/generate/$', dummydata.GenerateConnections.as_view(),
        name='generate-connections'),
    url(r'connection/delete/$', dummydata.DeleteConnections.as_view(),
        name='delete-connections'),
    url(r'message/send-bulk/$', dummydata.SendBulkMessage.as_view(),
        name='send-bulk-message'),
)
