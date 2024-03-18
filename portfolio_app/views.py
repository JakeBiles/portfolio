#views File
from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView
from .models import *
from .forms import *

# Create your views here.
def index(request):
    active_student_portfolios = Student.objects.select_related("portfolio").all().filter(portfolio__is_active = True)
    print("QUERY:: Students with Active portfolios? Response:",active_student_portfolios)
    return render( request, 'portfolio_app/index.html', {'active_student_portfolios':active_student_portfolios})

# Model views
class StudentListView(ListView):
    model = Student
    
class StudentDetailView(DetailView):
    model = Student
    
class PortfolioDetailView(DetailView):
    model = Portfolio

class ProjectDetailView(DetailView):
    model = Project
    
# Forms
def createProject(request, portfolio_id):
    form = ProjectForm()
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    
    if request.method == 'POST':
        project_data = request.POST.copy()
        project_data['portfolio_id'] = portfolio_id
        form = ProjectForm(project_data)
        
        if 'Cancel' in request.POST:
            return redirect('portfolio-detail',portfolio_id)
        
        elif form.is_valid():
            project = form.save(commit=False)
            project.portfolio = portfolio
            project.save()
            
            return redirect('portfolio-detail',portfolio_id)
    
    context = {'form': form}
    return render(request, 'portfolio_app/update_create_form.html', context)

def updateProject(request, project_id):
    project = Project.objects.get(pk=project_id)
    form = ProjectForm(instance=project)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        
        if 'Cancel' in request.POST:
            return redirect('portfolio-detail',project.portfolio.pk)
        
        elif form.is_valid():
            form.save()
            return redirect('project-detail',project_id)
    
    context = {'form': form}
    return render(request, 'portfolio_app/update_create_form.html', context)

def deleteProject(request, project_id):
    project = Project.objects.get(pk=project_id)

    if request.method == 'POST':
        
        if 'Cancel' in request.POST:
            return redirect('portfolio-detail',project.portfolio.pk)
        
        else:
            project.delete()
            return redirect('portfolio-detail',project.portfolio.pk)

    return render(request,
                    'portfolio_app/delete_form.html',
                    {'project': project})

def updatePortfolio(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    form = PortfolioForm(instance=portfolio)
    
    if request.method == 'POST':
        form = PortfolioForm(request.POST,instance=portfolio)
        
        if 'Cancel' in request.POST:
            return redirect('portfolio-detail',portfolio_id)
        
        elif form.is_valid():
            form.save()
            return redirect('portfolio-detail',portfolio_id)
    
    context = {'form': form}
    return render(request, 'portfolio_app/update_create_form.html', context)