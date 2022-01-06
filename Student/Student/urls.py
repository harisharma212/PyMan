"""Student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from MyApp import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('about/', views.about),
    path('service/', views.service),
    path('students/', views.students),
    path('add_student/', views.AddStudentView.as_view()),
    path('contact/', views.contact),
    path('search_student/', views.SearchStudentView.as_view()),
    path('view_student/<id>', views.ViewStudentView.as_view()),
    path('view_or_edit_Family/<id>', views.home),
    path('view_or_edit_GovtId/<id>', views.home),
    path('view_or_edit_Education/<id>', views.home),
    path('view_or_edit_Consultancy/<id>', views.home),
]
