"""grid_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from students.views import load_student_details
from students.views import server_side_filtering
from students.views import student_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/load-student-details/', load_student_details, name='load-student-details'),
    path('api/server-side-filtering/', server_side_filtering, name='server-side-filtering'),
    path('students/student_list.html', student_list, name='student_list'),


]
