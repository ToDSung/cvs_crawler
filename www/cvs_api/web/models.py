from django.db import models


# Create your models here.
class Cvs(models.Model):
    title = models.TextField()
    topic = models.IntegerField()
    article_time = models.TextField()
    article_link = models.TextField()
    message = models.IntegerField()
    push_count = models.IntegerField()
    push_message = models.TextField()
    bull_count = models.IntegerField()
    bull_message = models.TextField()
    arrow_count = models.IntegerField()
    arrow_message = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
