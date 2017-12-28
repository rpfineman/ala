#
#   FORMS
#
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime

class HackernewsForm(forms.Form):
    star = forms.BooleanField(required=False)
    notes = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':'16', 'cols':'128', 'autofocus':'true', 'wrap':'off'}))
    referrer = forms.CharField(required=False)
    def clean_star(self):
        data = self.cleaned_data['star']
        return data
    def clean_notes(self):
        data = self.cleaned_data['notes']
        return data
    def clean_referrer(self):
        data = self.cleaned_data['referrer']
        return data

class SlashdotForm(forms.Form):
    star = forms.BooleanField(required=False)
    notes = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':'16', 'cols':'128', 'autofocus':'true', 'wrap':'off'}))
    referrer = forms.CharField(required=False)
    def clean_star(self):
        data = self.cleaned_data['star']
        return data
    def clean_notes(self):
        data = self.cleaned_data['notes']
        return data
    def clean_referrer(self):
        data = self.cleaned_data['referrer']
        return data

class RedditForm(forms.Form):
    star = forms.BooleanField(required=False)
    notes = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':'16', 'cols':'128', 'autofocus':'true', 'wrap':'off'}))
    referrer = forms.CharField(required=False)
    def clean_star(self):
        data = self.cleaned_data['star']
        return data
    def clean_notes(self):
        data = self.cleaned_data['notes']
        return data
    def clean_referrer(self):
        data = self.cleaned_data['referrer']
        return data

class ChanForm(forms.Form):
    star = forms.BooleanField(required=False)
    notes = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':'16', 'cols':'128', 'autofocus':'true', 'wrap':'off'}))
    referrer = forms.CharField(required=False)
    def clean_star(self):
        data = self.cleaned_data['star']
        return data
    def clean_notes(self):
        data = self.cleaned_data['notes']
        return data
    def clean_referrer(self):
        data = self.cleaned_data['referrer']
        return data


