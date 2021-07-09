from django.db import models

# Create your models here.
class Article(models.Model): #Article is the table
    #the following attribites are the fields
    title = models.CharField(max_length= 100)
    description = models.TextField()

    '''
    By default, django assingd an id to the object and returns 
    it as the link name in the admin panel
    '''
    #add the following to give it your own name
    def __str__(self):
        return f'{self.title}'