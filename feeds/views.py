#
#   VIEWS
#
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Count
from django.shortcuts import render
from django.shortcuts import render_to_response
from django import template
register = template.Library()
from .models import Chan, Reddit, Slashdot, Hackernews
from django.views import generic
from django.views.generic import ListView
from django.views.generic import DetailView
from datetime import date
# for ModelForm
from django.http import HttpResponseRedirect

#graphviz = GraphvizOutput(output_file='filter_none.png')
#with PyCallGraph(output=graphviz):

# Home page
def index(request):
    c=Chan.objects.all()[0]
    r=Reddit.objects.all()[0]
    s=Slashdot.objects.all()[0]
    h=Hackernews.objects.all()[0]
    chan_record_count=Reddit.objects.all().count()
    reddit_record_count=Reddit.objects.all().count()
    slashdot_record_count=Slashdot.objects.all().count()
    hackernews_record_count=Hackernews.objects.all().count()
    return render(request, 'index.html',
                  context={'chan_record_count':chan_record_count,
                           'reddit_record_count':reddit_record_count,
                           'slashdot_record_count':slashdot_record_count,
                           'hackernews_record_count':hackernews_record_count,
                           'c':c,
                           'r':r,
                           's':s,
                           'h':h,
                          }
                  )
# List pages
class HackernewsListView(generic.ListView):
    model = Hackernews
class SlashdotListView(generic.ListView):
    model = Slashdot
class RedditListView(generic.ListView):
    model = Reddit
class ChanListView(generic.ListView):
    model = Chan
# Detail pages
class HackernewsDetailView(generic.DetailView):
    model = Hackernews
class SlashdotDetailView(generic.DetailView):
    model = Slashdot
class RedditDetailView(generic.DetailView):
    model = Reddit
class ChanDetailView(generic.DetailView):
    model = Chan

##################################################
#
#   F O R M S
#
##################################################
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.urls import reverse
import datetime
from django.contrib.auth.decorators import permission_required
from .forms import ChanForm, RedditForm, SlashdotForm, HackernewsForm

def hackernews_update(request, pk):
    record=get_object_or_404(Hackernews, pk=pk)
    if request.method == 'POST':
        form = HackernewsForm(request.POST)
        if form.is_valid():
            record.notes= form.cleaned_data['notes']
            record.star= form.cleaned_data['star']
            record.save()
        return redirect(form.cleaned_data['referrer'])
    else:
        s=record.star
        n=record.notes
        r=request.META['HTTP_REFERER']
        form = HackernewsForm(initial={'star':s, 'notes': n, 'referrer': r})
    return render(request, 'feeds/hackernews_update_form.html', {'form': form, 'record':record})
def hackernews_update_star(request, pk):
    record=get_object_or_404(Hackernews, pk=pk)
    if request.method == 'POST':
        form = HackernewsForm(request.POST) # Create a form instance and populate it with data from the request (binding):
        if form.is_valid(): # Check if the form is valid
            record.star= form.cleaned_data['star']
            record.save()
        return redirect(form.cleaned_data['referrer'])
    else:
        s=record.star
        r=request.META['HTTP_REFERER']
        form = HackernewsForm(initial={'star':s, 'referrer': r})
    return render(request, 'feeds/hackernews_update_star_form.html', {'form': form, 'record':record},)


def slashdot_update(request, pk):
    record=get_object_or_404(Slashdot, pk=pk)
    if request.method == 'POST':
        form = SlashdotForm(request.POST)
        if form.is_valid():
            record.notes= form.cleaned_data['notes']
            record.star= form.cleaned_data['star']
            record.save()
        return redirect(form.cleaned_data['referrer'])
    else:
        s=record.star
        n=record.notes
        r=request.META['HTTP_REFERER']
        form = HackernewsForm(initial={'star':s, 'notes': n, 'referrer': r})
    return render(request, 'feeds/slashdot_update_form.html', {'form': form, 'record':record})
def slashdot_update_star(request, pk):
    record=get_object_or_404(Slashdot, pk=pk)
    if request.method == 'POST':
        form = SlashdotForm(request.POST) # Create a form instance and populate it with data from the request (binding):
        if form.is_valid(): # Check if the form is valid
            record.star= form.cleaned_data['star']
            record.save()
        return redirect(form.cleaned_data['referrer'])
    else:
        s=record.star
        r=request.META['HTTP_REFERER']
        form = SlashdotForm(initial={'star':s, 'referrer': r})
    return render(request, 'feeds/slashdot_update_star_form.html', {'form': form, 'record':record},)


def reddit_update(request, pk):
    record=get_object_or_404(Reddit, pk=pk)
    if request.method == 'POST':
        form = RedditForm(request.POST)
        if form.is_valid():
            record.notes= form.cleaned_data['notes']
            record.star= form.cleaned_data['star']
            record.save()
        return redirect(form.cleaned_data['referrer'])
    else:
        s=record.star
        n=record.notes
        r=request.META['HTTP_REFERER']
        form = HackernewsForm(initial={'star':s, 'notes': n, 'referrer': r})
    return render(request, 'feeds/reddit_update_form.html', {'form': form, 'record':record})
def reddit_update_star(request, pk):
    record=get_object_or_404(Reddit, pk=pk)
    if request.method == 'POST':
        form = RedditForm(request.POST) # Create a form instance and populate it with data from the request (binding):
        if form.is_valid(): # Check if the form is valid
            record.star= form.cleaned_data['star']
            record.save()
        return redirect(form.cleaned_data['referrer'])
    else:
        s=record.star
        r=request.META['HTTP_REFERER']
        form = RedditForm(initial={'star':s, 'referrer': r})
    return render(request, 'feeds/reddit_update_star_form.html', {'form': form, 'record':record},)

def chan_update(request, pk):
    record=get_object_or_404(Chan, pk=pk)
    if request.method == 'POST':
        form = ChanForm(request.POST)
        if form.is_valid():
            record.notes= form.cleaned_data['notes']
            record.star= form.cleaned_data['star']
            record.save()
        return redirect(form.cleaned_data['referrer'])
    else:
        s=record.star
        n=record.notes
        r=request.META['HTTP_REFERER']
        form = ChanForm(initial={'star':s, 'notes': n, 'referrer': r})
    return render(request, 'feeds/chan_update_form.html', {'form': form, 'record':record})
def chan_update_star(request, pk):
    record=get_object_or_404(Chan, pk=pk)
    if request.method == 'POST':
        form = ChanForm(request.POST) # Create a form instance and populate it with data from the request (binding):
        if form.is_valid(): # Check if the form is valid
            record.star= form.cleaned_data['star']
            record.save()
        return redirect(form.cleaned_data['referrer'])
    else:
        s=record.star
        r=request.META['HTTP_REFERER']
        form = ChanForm(initial={'star':s, 'referrer': r})
    return render(request, 'feeds/chan_update_star_form.html', {'form': form, 'record':record},)


def saved(request):
    h=Hackernews.objects.raw( 'select * from feeds_hackernews where star==1 or (length(notes)>0);')
    s=Slashdot.objects.raw( 'select * from feeds_slashdot where star==1 or (length(notes)>0);')
    r=Reddit.objects.raw( 'select * from feeds_reddit where star==1 or (length(notes)>0);')
    c=Chan.objects.raw( 'select * from feeds_chan where star==1 or (length(notes)>0);')
    if h == '' or h == None:
        h=0
    return render(request, 'feeds/saved.html', context={'c':c, 'r':r, 's':s, 'h':h,},)



