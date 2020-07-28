from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class SignUp(TemplateView):
    template_name = "signup.html"

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        data_form = SignForm()
        context['form'] = data_form
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        register_form = SignForm(data=request.POST)
        if register_form.is_valid():
           register_form.save()
           return redirect("/login")
        else:
            print(register_form.errors)
            return render(request, self.template_name, {"form": register_form})


class SignForm(UserCreationForm):
    template_name = "signup.html"
