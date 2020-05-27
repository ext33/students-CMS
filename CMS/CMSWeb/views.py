from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import auth_logout
from CMSWeb.forms import LoginForm


# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


class Profile(TemplateView):
    template_name = 'profile.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            return render(request, self.template_name, )


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