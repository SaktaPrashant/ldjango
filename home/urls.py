from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [

    path('boy', views.home,name='home')

]

urlpatterns = [

    path('paths', views.paths,name='paths')

]