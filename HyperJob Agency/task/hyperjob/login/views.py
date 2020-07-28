from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import Http404
from django.contrib.auth import authenticate, login

# Create your views here.
class Login(TemplateView):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        data_form = LoginForm()
        context['form'] = data_form
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
        raise Http404("pff pff")


class LoginForm(AuthenticationForm):
    pass