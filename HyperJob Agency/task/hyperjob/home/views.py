from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.exceptions import PermissionDenied
from django.contrib.auth import models
from django import forms


# Create your views here.

class Home(TemplateView):
    template_name = "home/home.html"

    def get(self, request, *args, **kwargs):
        context = super().get_context_data()
        try:
            user = models.User.objects.get(id=request.user.id)
        except Exception:
            context['is_user'] = False
            return render(request, self.template_name, context)
        context["is_user"] = True
        if user.is_staff:
            context['btn_url'] = "/vacancy/new"
            context['btn_label'] = "New Vacancy"
            context['form'] = VacancyForm()
        else:
            context['btn_url'] = "/resume/new"
            context['btn_label'] = "New resume"
            context['form'] = ResumeForm()
        return render(request, self.template_name, context)

class VacancyForm(forms.Form):
    description = forms.CharField(max_length=255)

class ResumeForm(forms.Form):
    description = forms.CharField(max_length=255)
