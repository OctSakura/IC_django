from django.shortcuts import render
from .models import Entry

def index(request):
    return render(request, 'index.html')

def blog(request):
    entries = Entry.objects.all()
    context = {'entries' : entries}
    return  render(request, 'blog/blog.html',context)