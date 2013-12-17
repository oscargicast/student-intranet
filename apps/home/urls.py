from django.conf.urls.defaults import *
from .views import login_view, logout_view, add_student, delete_student


urlpatterns = patterns('',
    url(r'^$', login_view, name='login_view'),
    url(r'^logout/$', logout_view, name='logout_view'),
    url(r'^add/$', add_student, name='add_student_view'),
    url(r'^delete/$', delete_student, name='delete_student_view'),
)