from django import forms
from .models import User, Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserChangeForm

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title','description','due_date', 'priority_level')

class LoginForm(AuthenticationForm):
    pass

class UpdateProfileForm(UserChangeForm):
    password = None  # Remove the password field from the update form

    class Meta:
        model = User
        fields = ['username', 'email',]