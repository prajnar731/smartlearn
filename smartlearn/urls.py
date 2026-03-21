from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('login/student/', auth_views.LoginView.as_view(template_name='registration/student_login.html'), name='student_login'),
    path('login/faculty/', auth_views.LoginView.as_view(template_name='registration/faculty_login.html'), name='faculty_login'),
    
]
