from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    """
    models for blog
    """
    title = models.CharField(max_length=32, default="Title")
    content = models.TextField(null=True)
    """
    Return the title
    """
    def __unicode__(self):
        return self.title

# Create your models here.
class Message(models.Model):
    """
    models for Message
    """
    content = models.TextField(null=True)
    """
    display the content
    """
    def __unicode__(self):
        return self.content
