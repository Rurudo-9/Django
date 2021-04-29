from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):

    # Topic class only have tow attributes: text & date_added

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Entry(models.Model):

    # Entry as a foreign key at Topic (build relation btw Entry & Topic)
    # Topic ID restored to topic
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..." # only see the first 50 instead of all of them
    



