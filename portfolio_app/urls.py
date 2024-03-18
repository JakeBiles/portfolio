from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('students/',views.StudentListView.as_view(),name='student-list'),
    path('students/<int:pk>',views.StudentDetailView.as_view(),name='student-detail'),
    path('portfolio/<int:pk>',views.PortfolioDetailView.as_view(),name='portfolio-detail'),
    path('portfolio/<int:portfolio_id>/add_project', views.createProject, name='create-project'),
    path('portfolio/<int:portfolio_id>/update_portfolio',views.updatePortfolio, name='update-portfolio'),
    path('project/<int:pk>',views.ProjectDetailView.as_view(),name='project-detail'),
    path('project/<int:project_id>/update_project', views.updateProject, name='update-project'),
    path('project/<int:project_id>/delete_project', views.deleteProject, name='delete-project'),
    
]
