from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
# from django.contrib.auth import get_user_model
# from apps.login.models import MyUser
# from apps.pcb.models import Pcb


def home(request):
    return render_to_response(
        'home/index.html',
        context_instance=RequestContext(request)
    )
