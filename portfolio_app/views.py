from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import *
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    active_student_portfolios = Student.objects.select_related("portfolio").all().filter(portfolio__is_active=True)
    print("QUERY:: Students with Active portfolios? Response:",active_student_portfolios.select_related('portfolio'))
    return render( request, 'portfolio_app/index.html', {'active_student_portfolios':active_student_portfolios})

class StudentListView(ListView):
    model = Student
    
class StudentDetailView(DetailView):
    model = Student
