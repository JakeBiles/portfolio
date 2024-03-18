from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title','desc')
        
class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ('title','about','is_active','contact_email')
        