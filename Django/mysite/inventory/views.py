from django.shortcuts import render
from .models import Entry
from django.db.models import Count

def inv(request):
    entries_all = Entry.objects.all()
    entries_more_than = Entry.objects.filter(Price__gte = 10000)
    entries_5_year = Entry.objects.filter(Acq_date__year__lte = 2018)
    loc_count = Entry.objects.values('Location').annotate(total_inventory = Count('id'))
    user_count = Entry.objects.values('End_user').annotate(total_user = Count('id'))
    context = {'entries': entries_all,'entries1' : entries_more_than, 'entries2' : entries_5_year, 'loc_count' : loc_count, 'user_count' : user_count}
    return  render(request, 'inventory/inv.html', context)

def index(request):
    return render(request, 'index.html')