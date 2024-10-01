from django.db.models.base import Model as Model
from django.forms import BaseModelForm
from django.http import HttpResponseForbidden
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from rest_framework import generics
from django.contrib.auth.views import LogoutView
from .models import Task, User
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer, UserSerializer
from django.views.generic import CreateView
from .forms import UserRegistrationForm
from .forms import TaskForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from .forms import UpdateProfileForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView


class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'for_user/profile.html'


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    seliarizer_class = UserSerializer

class TaskList(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'for_tasks/task_list.html'  

    def get_queryset(self):
        # Start with tasks belonging to the logged-in user
        queryset = Task.objects.filter(user=self.request.user)

        # Get filter parameters from the request
        status = self.request.GET.get('status')
        priority = self.request.GET.get('priority')
        due_date = self.request.GET.get('due_date')

        # Apply filters if the corresponding parameters are present
        if status:
            queryset = queryset.filter(status=status)
        if priority:
            queryset = queryset.filter(priority=priority)
        if due_date:
            queryset = queryset.filter(due_date=due_date)

        # Apply sorting based on query parameter 'ordering'
        ordering = self.request.GET.get('ordering', 'due_date')  # default to 'due_date'
        
        if ordering == 'pending_first':
            queryset = queryset.order_by('-is_complete', 'due_date')  # Pending tasks first
        elif ordering == 'priority_high_to_low':
            queryset = queryset.order_by('-priority_level', 'due_date')  # Highest priority first
        else:
            queryset = queryset.order_by(ordering)

        return queryset

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'for_tasks/task_update.html'  # Create this template
    fields = ('title', 'description', 'due_date', 'priority_level')

    def get_object(self):
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        if task.user != self.request.user:
            raise PermissionDenied  # Automatically returns a 403 error
        return task
    
    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()

        # Prevent editing if task is complete
        if task.is_complete:
            messages.error(request, "You cannot edit a completed task. Mark it as incomplete first.")
            return redirect('task_list')

        return super().dispatch(request, *args, **kwargs)
    def get_object(self):
        return get_object_or_404(Task, pk=self.kwargs['pk'], user=self.request.user)
    
    def get_success_url(self):
        return reverse_lazy('task_list')
    

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'for_tasks/task_delete_confirm.html'

    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except Exception as e:
            messages.error(self.request, "There was an error deleting the task.")
            return HttpResponse(status=500)
    def get_success_url(self):
        return reverse_lazy('task_list')


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegisterView(CreateView):
    template_name = 'for_user/register.html'
    form_class = UserRegistrationForm


    def form_valid(self, form):
        self.object = form.save()
        return redirect('login')
    
    def get_success_url(self):
        return reverse_lazy('login')
    
class TaskCreateView(LoginRequiredMixin,CreateView):
    template_name = 'for_tasks/create.html'
    form_class = TaskForm
    model = Task
    success_url = reverse_lazy('task/create')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the task to the logged-in user
        response = super().form_valid(form)
        messages.success(self.request, 'Task created successfully!')
        print(self.request._messages)
        return response
    
    def get_success_url(self):
        return reverse_lazy('task_list')

class CustomLoginView(LoginView):
    template_name = 'for_user/login.html'
    def form_valid(self, form):
        # Adding a success message after successful login
        messages.success(self.request, 'Successfully logged in!')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('homepage')

class HomepageView(LoginRequiredMixin,TemplateView):
    template_name= 'for_tasks/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class TaskToggleCompleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)

        # Check if the task is already complete and toggle it
        if task.is_complete:
            task.mark_as_incomplete()
            messages.success(request, "Task marked as incomplete.")
        else:
            task.mark_as_complete()
            messages.success(request, "Task marked as complete.")
        
        return redirect('task_list')

class MarkCompleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.mark_as_complete()  # Mark the task as complete
        messages.success(request, f"Task '{task.title}' marked as complete.")
        return redirect('task_list')

class MarkIncompleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.mark_as_incomplete()  # Mark the task as incomplete
        messages.success(request, f"Task '{task.title}' marked as incomplete.")
        return redirect('task_list')

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UpdateProfileForm
    template_name = 'for_user/update_profile.html'
    success_url =reverse_lazy('profile')

    def get_object(self):
        return self.request.user

class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'for_user/delete_account.html'
    success_url = reverse_lazy('homepage')  # Redirect after deleting

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Your account has been deleted successfully.')
        return super().delete(request, *args, **kwargs)