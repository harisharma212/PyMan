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
    path('contact/', views.contact),

    path('batches/', views.batches),
    path('add_batch/', views.AddBatchView.as_view()),
    path('view_bacth/<id>/', views.SearchbacthView.as_view()),

    path('students/', views.students),
    path('add_student/', views.AddStudentView.as_view()),
    path('search_student/', views.SearchStudentView.as_view()),
    path('view_student/<id>', views.ViewStudentView.as_view()),
    path('delete_student/<id>', views.delete_student),
    path('edit_student/<id>', views.EditStudentView.as_view()),
    
    path('viewFamily/<id>', views.view_family),
    path('editFamily/<id>', views.EditFamily.as_view()),
    path('addFamily/<id>', views.AddFamilyView.as_view()),
    path('deleteFamily/<id>', views.delete_family),

    path('viewGovtId/<id>', views.view_govtId),
    path('editGovtId/<id>', views.EditGovtIdView.as_view()),
    path('addGovtId/<id>', views.AddGovtIdView.as_view()),
    path('deleteGovtId/<id>', views.delete_govtId),

    path('viewEducation/<id>', views.view_education),
    path('editEducation/<id>', views.EditEducationView.as_view()),
    path('addEducation/<id>', views.AddEducationView.as_view()),
    path('deleteEducation/<id>', views.delete_education),

    path('viewCourseFeeDetails/<id>', views.view_course_fee),
    path('editCourseFeeDetails/<id>', views.EditCourseFeeDetailsView.as_view()),
    path('addCourseFeeDetails/<id>', views.AddCourseFeeView.as_view()),
    path('deleteCourseFeeDetails/<id>', views.delete_course_fee),

    path('viewConsultancy/<id>', views.view_consultancy),
    path('editConsultancy/<id>', views.EditConsultancyView.as_view()),
    path('addConsultancy/<id>', views.AddConsultancyView.as_view()),
    path('deleteConsultancy/<id>', views.delete_consultancy),
    
]


# test with github (For testing purpose)....