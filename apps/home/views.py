from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.home.forms import LoginForm, RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from apps.students.models import Student


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


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password_one = form.cleaned_data['password_one']
            password_two = form.cleaned_data['password_two']
            u = User.objects.create_user(
                username=usuario, email=email, password=password_one)
            u.save()  # Guardar el objeto
            
            student = Student()
            student.user = u
            student.career = form.cleaned_data['career']
            student.save()
            return render_to_response(
                'home/index.html',
                context_instance=RequestContext(request)
            )
        else:
            ctx = {'form': form}
            return render_to_response(
                'home/register.html',
                ctx,
                context_instance=RequestContext(request)
            )
    ctx = {'form': form}
    return render_to_response(
        'home/register.html',
        ctx,
        context_instance=RequestContext(request)
    )


def delete_student(request):
    return render_to_response(
        'home/index.html',
        context_instance=RequestContext(request)
    )
