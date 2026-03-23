from django.shortcuts import render
from .models import Subject

def student_dashboard(request):
    subjects = Subject.objects.all()
    return render(request, 'student-dashboard.html', {'subjects': subjects})
