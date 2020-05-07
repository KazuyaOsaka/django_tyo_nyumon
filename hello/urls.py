from django.conf.urls import url
from django.urls import path
# from .views import HelloView
from . import views

urlpatterns = [
    # url('', HelloView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
]