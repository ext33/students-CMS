from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import auth_logout
from CMSWeb.forms import LoginForm
from .models import Performance

# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


class Profile(TemplateView):
    template_name = 'profile.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            if request.user.is_staff:
                return render(request, self.template_name)
            else:
                perf = {}

                if Performance.objects.filter(FIO=request.user):
                    for obj in Performance.objects.filter(FIO=request.user):
                        obj.data = [obj.subject, obj.mark, obj.reporting_form]
                        perf[obj.date] = obj.data

            tup_len = len(perf)
            return render(request, self.template_name, context={'perf': perf, 'tup_len': tup_len})


class Login(TemplateView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        error = ''

        if request.user.is_authenticated:
            return redirect('profile')
        else:
            if request.method == 'POST':
                if form.is_valid():
                    username = form.cleaned_data['username']
                    password = form.cleaned_data['password']
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('profile')
                    else:
                        error = 'Такого пользователя не существует'
                else:
                    error = 'Логин или пароль неправильные'

            return render(request, self.template_name, {'form': form, 'error': error})


def logout(request):
    auth_logout(request)
    return redirect('login')