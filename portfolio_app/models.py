from django.db import models
from django.urls import reverse

# Create your models here.
# Portfolio
class Portfolio(models.Model):
    title = models.CharField(max_length = 200)
    contact_email =  models.CharField(max_length = 200)
    is_active = models.BooleanField(default=True,)
    about = models.CharField(max_length = 1000, blank = True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("portfolio-detail", args=[str(self.id)])
    
# Project
class Project(models.Model):
    title = models.CharField(max_length = 200)
    desc = models.CharField(max_length = 1000)
    portfolio = models.ForeignKey(Portfolio, null=True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("project-detail", args=[str(self.id)])

# Student
class Student(models.Model):
    MAJOR = (
        ('CSCI-BS', 'BS in Computer Science'),
        ('CPEN-BS', 'BS in Computer Engineering'),
        ('BIGD-BI', 'BI in Game Design and Development'),
        ('BICS-BI', 'BI in Computer Science'),
        ('BISC-BI', 'BI in Computer Security'),
        ('CSCI-BA', 'BA in Computer Science'),
        ('DASE-BS', 'BS in Data Analytics and Systems Engineering')
    )
    
    name = models.CharField(max_length = 200)
    email = models.CharField("UCCS EMAIL", max_length = 200)
    major = models.CharField(max_length = 200, choices=MAJOR)
    portfolio = models.ForeignKey(Portfolio, null=True, on_delete = models.SET_NULL)

    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("student-detail", args=[str(self.id)])


