from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=256)
    article_text = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)

class Skill(models.Model):
    title = models.CharField(max_length=256)
    skill_text = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
