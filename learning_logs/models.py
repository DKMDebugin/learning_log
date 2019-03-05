from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    '''A topic the user is learning about'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        '''Return a string representation of the model'''
        return self.text

class Entry(models.Model):
    '''Something specific learned about a topic'''
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''
        Holds extra info for managing a model.
        Here it allows us set a special attribute telling
        Django to use Entries when it needs to refer to more than on entry.
        '''
        verbose_name_plural = 'entries'

    def __str__(self):
        '''return the first 50 character of a string representation of the model'''
        if len(self.text) <= 50:
            return self.text
        return self.text[:50] + '...'
