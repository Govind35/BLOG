from django.db import models
from django.utils import timezone #for time
from django.contrib.auth.models import User #
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete= models.CASCADE )

    def __str__(self):
        return self.title

    def get_absolute_url(self):     # used to show the new post created
        return reverse('post-detail', kwargs={'pk': self.pk}) # reverse will take to post-detail url with value of pk

    