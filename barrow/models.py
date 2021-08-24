from django.db import models
from django.urls import reverse

# Create your models here.
class Barrow(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publish = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)
    flag = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail',kwargs={'id':self.id})
        #return "/books/{}".format(self.id)
