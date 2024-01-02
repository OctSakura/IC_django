from django.shortcuts import render,redirect
from .models import Entry
from .forms import EntryForm

def index(request):
    return render(request, 'index.html')

def blog(request):
    entries = Entry.objects.order_by('-date_posted')
    context = {'entries' : entries}
    return  render(request, 'blog/blog.html',context)

def add(request):
    if request.method=='POST':
        form = EntryForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/blog/')
    else:
        form = EntryForm()

    context = {'form' : form}
    return render(request, 'blog/add.html', context)