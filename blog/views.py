from django.shortcuts import render
from .models import Blog


def allblogs(request):
        blog = Blog.objects
        return render(request, 'allblogs.html', {'blog': blog})
