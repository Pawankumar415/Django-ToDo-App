from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.CustomLoginView.as_view(),name = 'login'),
    path('logout/',views.UserLogoutView.as_view(),name = 'logout'),
    path('register/',views.RegisterPage.as_view(),name = 'register'),
    path('',views.TaskListView.as_view(),name = 'task-list'),
    path('task/<int:pk>/',views.TaskDetailView.as_view(),name = 'task-detail'),
    path('create/',views.TaskCreateView.as_view(),name = 'task-create'),
    path('task-update/<int:pk>/',views.TaskUpdateView.as_view(),name = 'task-update'),
    path('task-delete/<int:pk>/',views.TaskDeleteView.as_view(),name = 'task-delete'),
]