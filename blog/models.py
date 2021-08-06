from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateField()
    image=models.ImageField(blank=True,default='default.png')

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:30]+'...'

class Comment(models.Model):
    content = models.TextField()    
    date = models.DateField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.content