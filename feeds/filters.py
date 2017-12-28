#
#   FILTERS (django_filters)
#
from django.forms import MultiWidget
from distutils.util import strtobool
from datetime import date
from django.forms import widgets
from django_filters.views import FilterView
from django import forms
import django_filters
from django_filters import filters
from django_filters import *
from django_filters.widgets import *
from .models import Chan, Reddit, Hackernews, Slashdot


class HackernewsFilter(django_filters.FilterSet):
    title=django_filters.CharFilter(name="title", lookup_expr='icontains', widget=forms.TextInput(attrs={'style': 'width:260px'}))
    author=django_filters.CharFilter(name="author", lookup_expr='icontains', widget=forms.TextInput(attrs={'style': 'width:260px'}))

    num_comments__gte=django_filters.AllValuesFilter(name='num_comments', lookup_expr='gte', widget=forms.Select(attrs={'style':'width:110px'}))
    num_comments__lte=django_filters.AllValuesFilter(name='num_comments', lookup_expr='lte', widget=forms.Select(attrs={'style':'width:110px'}))

    date__gte=django_filters.AllValuesFilter(name='date', lookup_expr='gte')
    date__lte=django_filters.AllValuesFilter(name='date', lookup_expr='lte')

    notes=django_filters.CharFilter(name='notes', lookup_expr=None)
    star= django_filters.BooleanFilter(name='star', widget=BooleanWidget())

    o = django_filters.OrderingFilter(
            fields=(
                    ('title', 'title'),
                    ('author', 'author'),
                    ('num_comments', 'num_comments'),
                    ('date', 'date'),
                    ('notes', 'notes'),
                    ('star', 'star'),
            ))

    class Meta:
        model = Hackernews
        exclude= [
            'title',
            'notes',
            'star',
            'title',
            'num_comments',
            'url',
            'date',
        ]



class SlashdotFilter(django_filters.FilterSet):
    title=django_filters.CharFilter(name="title", lookup_expr='icontains', widget=forms.TextInput(attrs={'style': 'width:260px'}))
    author=django_filters.CharFilter(name="author", lookup_expr='icontains', widget=forms.TextInput(attrs={'style': 'width:260px'}))

    num_comments__gte=django_filters.AllValuesFilter(name='num_comments', lookup_expr='gte', widget=forms.Select(attrs={'style':'width:110px'}))
    num_comments__lte=django_filters.AllValuesFilter(name='num_comments', lookup_expr='lte', widget=forms.Select(attrs={'style':'width:110px'}))

    date__gte=django_filters.AllValuesFilter(name='date', lookup_expr='gte')
    date__lte=django_filters.AllValuesFilter(name='date', lookup_expr='lte')

    notes=django_filters.CharFilter(name='notes', lookup_expr=None)
    star= django_filters.BooleanFilter(name='star', widget=BooleanWidget())

    o = django_filters.OrderingFilter(
            fields=(
                    ('num_comments', 'num_comments'),
                    ('date', 'date'),
                    ('title', 'title'),
                    ('author', 'author'),
                    ('star', 'star'),
                    ('notes', 'notes'),
            ))

    class Meta:
        model = Slashdot
        exclude= [
            'title',
            'star',
            'title',
            'notes',
            'author',
            'num_comments',
            'url',
            'date',
        ]


class RedditFilter(django_filters.FilterSet):
    title=django_filters.CharFilter(name="title", lookup_expr='icontains', widget=forms.TextInput(attrs={'style': 'width:260px'}))
    author=django_filters.CharFilter(name="author", lookup_expr='icontains', widget=forms.TextInput(attrs={'style': 'width:260px'}))

    num_comments__gte=django_filters.AllValuesFilter(name='num_comments', lookup_expr='gte', widget=forms.Select(attrs={'style':'width:110px'}))
    num_comments__lte=django_filters.AllValuesFilter(name='num_comments', lookup_expr='lte', widget=forms.Select(attrs={'style':'width:110px'}))

    date__gte=django_filters.AllValuesFilter(name='date', lookup_expr='gte')
    date__lte=django_filters.AllValuesFilter(name='date', lookup_expr='lte')

    notes=django_filters.CharFilter(name='notes', lookup_expr=None)
    star= django_filters.BooleanFilter(name='star', widget=BooleanWidget())

    o = django_filters.OrderingFilter(
            fields=(
                    ('num_comments', 'num_comments'),
                    ('date', 'date'),
                    ('title', 'title'),
                    ('author', 'author'),
                    ('star', 'star'),
                    ('notes', 'notes'),
            ))

    class Meta:
        model = Reddit
        exclude= [
            'title',
            'star',
            'title',
            'notes',
            'author',
            'num_comments',
            'url',
            'date',
        ]


class ChanFilter(django_filters.FilterSet):
    title=django_filters.CharFilter(name="title", lookup_expr='icontains', widget=forms.TextInput(attrs={'style': 'width:260px'}))
    subject=django_filters.CharFilter(name="subject", lookup_expr='icontains', widget=forms.TextInput(attrs={'style': 'width:260px'}))

    num_comments__gte=django_filters.AllValuesFilter(name='num_comments', lookup_expr='gte', widget=forms.Select(attrs={'style':'width:110px'}))
    num_comments__lte=django_filters.AllValuesFilter(name='num_comments', lookup_expr='lte', widget=forms.Select(attrs={'style':'width:110px'}))

    date__gte=django_filters.AllValuesFilter(name='date', lookup_expr='gte')
    date__lte=django_filters.AllValuesFilter(name='date', lookup_expr='lte')

    notes=django_filters.CharFilter(name='notes', lookup_expr=None)
    star= django_filters.BooleanFilter(name='star', widget=BooleanWidget())

    o = django_filters.OrderingFilter(
            fields=(
                    ('num_comments', 'num_comments'),
                    ('date', 'date'),
                    ('title', 'title'),
                    ('subject', 'subject'),
                    ('star', 'star'),
                    ('notes', 'notes'),
            ))

    class Meta:
        model = Chan
        exclude= [
            'title',
            'subject',
            'star',
            'title',
            'notes',
            'author',
            'num_comments',
            'url',
            'date',
        ]



