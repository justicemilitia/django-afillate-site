from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^gifts-for-men/$',gifts_formen_view.as_view() , name='home'),
    url(r'^gifts-for-women/$',gifts_forwomen_view.as_view() , name='home'),
    # url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    # url(r'^create/$', post_create, name='create'),
    # url(r'^update/$', post_update, name='update'),
    # url(r'^delete/$', post_delete, 'delete')
]