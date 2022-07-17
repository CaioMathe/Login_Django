from django.contrib import admin
from django.urls import path, include
from . import view

urlpatterns = [
    path('', view.index, name='index'),
    path('accounts/', include('allauth.urls')),

]
