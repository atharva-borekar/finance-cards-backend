from django.urls import path
from . import views

urlpatterns = [
    path('api_overview', views.apiOverview, name='api-overview'),
    path('', views.todoList, name='todo-list'),
    path('create', views.todoCreate, name='todo-create'),
    path('update/<str:pk>', views.todoUpdate, name='todo-update'),
    path('delete/<str:pk>', views.todoDelete, name='todo-delete'),
]
