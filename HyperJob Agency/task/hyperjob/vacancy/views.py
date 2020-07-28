from django.shortcuts import render, redirect
from vacancy.models import Vacancy
from django.views.generic import TemplateView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django import forms
# Create your views here.

def vacancy_index(request, *args, **kwargs):
    return render(request, template_name="vacancy/Index.html", context=dict(Vacancy=Vacancy.objects.all()))

class New(TemplateView):
    template_name = "vacancy/new.html"

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        context = super().get_context_data()
        context['form'] = VacancyForm()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        description = request.POST['description']
        form = VacancyForm(data=request.POST)
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            if user.is_staff:
                vacancy = Vacancy(description=description, author_id=user.id)
                vacancy.save()
                return redirect("/home")
            else:
                raise PermissionDenied
        else:
            return render(request, self.template_name, {"form": form})


class VacancyForm(forms.Form):
    description = forms.CharField(max_length=255)
