from django.conf.urls.defaults import *
from .views import home
# from .views import login, logout, signup_view


urlpatterns = patterns('',
    url(r'^$', home, name='home_view'),
    # url(r'^logout/$', logout, name='logout'),
    # url(r'^registro/$', signup_view, name='signup'),
)