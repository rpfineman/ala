#
#   MODELS
#
import datetime
from django.utils import timezone
from django.urls import reverse
from django.db import models
from django import forms # For forms.BooleanField

class Hackernews(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    url = models.URLField(max_length=500, null=True, blank=True)
    num_comments = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True, db_index=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    notes = models.CharField(max_length=500, null=True, blank=True)
    star = models.BooleanField(default=False)
    class Meta:
        ordering = ['-date', '-num_comments']
    def get_absolute_url(self):
        return reverse('hackernews-detail', args=[str(self.id)])
    def __str__(self):
        return '%s,%s' % (self.id, self.title)

class Slashdot(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    url = models.URLField(max_length=500, null=True, blank=True)
    num_comments = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True, db_index=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    notes = models.CharField(max_length=500, null=True, blank=True)
    star = models.BooleanField(default=False)
    class Meta:
        ordering = ['-date', '-num_comments']
    def get_absolute_url(self):
        return reverse('slashdot-detail', args=[str(self.id)])
    def __str__(self):
        return '%s,%s' % (self.id, self.title)

class Reddit(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    url = models.URLField(max_length=500, null=True, blank=True)
    num_comments = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True, db_index=True)
    author = models.CharField(max_length=100, null=True, blank=True)
#    notes = models.CharField(max_length=500, null=True, blank=True)
    notes = models.CharField(max_length=500, default='', blank=True)
    star = models.BooleanField(default=False)
    class Meta:
        ordering = ['-date', '-num_comments']
    def get_absolute_url(self):
        return reverse('reddit-detail', args=[str(self.id)])
    def __str__(self):
        return '%s,%s' % (self.id, self.title)

class Chan(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    url = models.URLField(max_length=500, null=True, blank=True)
    num_comments = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True, db_index=True)
    notes = models.CharField(max_length=500, default='', blank=True)
    star = models.BooleanField(default=False)
    md5 = models.CharField(max_length=100, default='', blank=True)
    subject = models.CharField(max_length=500, default='', blank=True)
    class Meta:
        ordering = ['-date', '-num_comments']
    def get_absolute_url(self):
        return reverse('reddit-detail', args=[str(self.id)])
    def __str__(self):
        return '%s,%s' % (self.id, self.title)



