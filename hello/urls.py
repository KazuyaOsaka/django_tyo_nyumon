from django.conf.urls import url
from django.urls import path
# from .views import HelloView
from . import views

urlpatterns = [
    # url('', HelloView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('create', views.create, name='create')
,]