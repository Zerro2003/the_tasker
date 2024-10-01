from rest_framework import routers
from . import views
from django.contrib.auth import views as auth_views
from .views import HomepageView
from .views import TaskList
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import ProfileView
from . views import TaskToggleCompleteView
from .views import MarkCompleteView, MarkIncompleteView
from .views import UpdateProfileView
from .views import DeleteUserView


router = routers.DefaultRouter() 
urlpatterns = [
    path('', include(router.urls)),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('tasks/create/',views.TaskCreateView.as_view(), name='task_create'),
    path('login/', views.CustomLoginView.as_view(),name='login'),
    path('homepage/',HomepageView.as_view(), name='homepage'),
    path('task/',TaskList.as_view(),name='task_list'),
    path('tasks/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('profile/',ProfileView.as_view(), name='profile'),
    path('task/<int:pk>/toggle_complete/', TaskToggleCompleteView.as_view(), name='task_toggle_complete'),
    path('task/<int:pk>/complete/', MarkCompleteView.as_view(), name='task_mark_complete'),
    path('task/<int:pk>/incomplete/', MarkIncompleteView.as_view(), name='task_mark_incomplete'),
    path('profile/update/', UpdateProfileView.as_view(), name='update_profile'),
    path('profile/delete/', DeleteUserView.as_view(), name='delete_account'),
    
]