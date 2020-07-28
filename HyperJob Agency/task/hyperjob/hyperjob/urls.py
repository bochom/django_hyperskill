from main_menu.views import MainMenu
from vacancy.views import vacancy_index
import vacancy.views
from resume.views import resume_index
from signup.views import SignUp
from login.views import Login
from home.views import Home
import resume

"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", MainMenu.as_view()),
    path("vacancies", vacancy_index),
    path("resumes", resume_index),
    path("signup", SignUp.as_view()),
    path("login", Login.as_view()),
    path("home", Home.as_view()),
    path("resume/new", resume.views.New.as_view()),
    path("vacancy/new", vacancy.views.New.as_view()),
]
