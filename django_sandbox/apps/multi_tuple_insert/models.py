from django.db import models
from django.utils.translation import ugettext as _


class Author(models.Model):
    name = models.CharField(max_length=40, verbose_name=_('name'))
    age = models.PositiveSmallIntegerField(verbose_name=_('age'))
    website = models.URLField(verbose_name=_('website'))
    notes = models.CharField(max_length=120, default='', verbose_name=_('notes'))


class Book(models.Model):
    author = models.ForeignKey(Author, verbose_name=_('author'))
    title = models.CharField(max_length=40, verbose_name=_('title'))
    published = models.DateField(verbose_name=_('published'))
    summary = models.CharField(max_length=256, default='', verbose_name=_('summary'))