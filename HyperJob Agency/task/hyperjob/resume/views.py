from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from resume.models import Resume
from django import forms
from django.views.generic import TemplateView
from django.contrib.auth.models import User

# Create your views here.

def resume_index(request):
    resume = Resume.objects.all()
    return render(request, template_name="resume/index.html", context=dict(resumes=resume))


class New(TemplateView):
    template_name = "resume/new.html"

    def get(self, request, *args, **kwargs):
        context = super().get_context_data()
        context['form'] = ResumeForm()
        if not request.user.is_authenticated:
            raise PermissionDenied
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        form = ResumeForm(data=request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            user = User.objects.get(id=request.user.id)
            new_resume = Resume(author=user, description=description)
            new_resume.save()
            return redirect("/home")
        else:
            return render(request, self.template_name, {"form":form})

class ResumeForm(forms.Form):
    description = forms.CharField(max_length=255)