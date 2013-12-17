from django.conf.urls.defaults import *
from .views import login_view, logout_view, register, delete_student


urlpatterns = patterns('',
    url(r'^$', login_view, name='login_view'),
    url(r'^logout/$', logout_view, name='logout_view'),
    url(r'^register/$', register, name='register_view'),
    url(r'^delete/$', delete_student, name='delete_student_view'),
)