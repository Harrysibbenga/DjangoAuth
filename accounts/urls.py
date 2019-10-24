from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/logout/', views.logout, name='logout')
]