from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.home.forms import StudentForm, LoginForm, RegisterForm
from django.contrib.auth import login, logout, authenticate


def login_view(request):
    message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                message = "usuario y/o password incorrecto"

    form = LoginForm()
    ctx = {'form': form, 'message': message}
    return render_to_response(
        'home/index.html',
        ctx,
        context_instance=RequestContext(request)
    )


def logout_view(request):
        logout(request)
        return HttpResponseRedirect('/')


def add_student(request):
    return render_to_response(
        'home/index.html',
        context_instance=RequestContext(request)
    )


def delete_student(request):
    return render_to_response(
        'home/index.html',
        context_instance=RequestContext(request)
    )
