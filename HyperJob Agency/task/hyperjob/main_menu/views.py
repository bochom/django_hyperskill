from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class MainMenu(TemplateView):
    resumes = []
    vacancies = []
    template_name = "main_menu/index.html"

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancies'] = self.vacancies
        context['resumes'] = self.resumes
        return render(request, self.template_name, context=context)
