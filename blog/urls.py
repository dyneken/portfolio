from django.contrib import admin
from django.urls import path, include
import blog.views


urlpatterns = [
    path('', blog.views.allblogs, name='allblogs'),
]