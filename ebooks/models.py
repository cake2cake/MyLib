from django.db import models

# Create your models here.

class Ebook(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100)
    pub_year = models.IntegerField()
    edition = models.IntegerField()
    file_name = models.CharField(max_length=200)
    def __str__(self):
        return  self.title






