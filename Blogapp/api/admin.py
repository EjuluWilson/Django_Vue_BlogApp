from django.contrib import admin

# Register your models here.
from .models import Article

# regidtering the article model
@admin.register(Article) 

#customising  the admin page
# you can modyfy the admin panel using the overr 30 attributes of ModelAdmin 
# below is an example

class ArticleModel(admin.ModelAdmin):
    list_filter = ('title', 'description') #filter using thes columns
    list_display = ('title', 'description')