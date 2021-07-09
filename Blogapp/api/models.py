from django.db import models

# Create your models here.
class Article(models.Model): #Article is the table
    #the following attribites are the fields
    title = models.CharField(max_length= 100)
    description = models.TextField()