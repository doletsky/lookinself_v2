from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="uploads/article/")
    short = models.TextField()
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    sort = models.IntegerField(default=1)
    test = models.IntegerField(default=None)
    image_a = models.ImageField(upload_to="uploads/article/")
    image_b = models.ImageField(upload_to="uploads/article/")
    image_c = models.ImageField(upload_to="uploads/article/")
    image_d = models.ImageField(upload_to="uploads/article/")
    image_f = models.ImageField(upload_to="uploads/article/")
# Create your models here.
