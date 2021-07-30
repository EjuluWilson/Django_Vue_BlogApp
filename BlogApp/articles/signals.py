from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Article
from django.utils.text import slugify

@receiver(pre_save, sender=Article)
def add_slug(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        instance.slug = slug
    
'''
article is the sender and add_slug is the receiver
the pre_save signal sends the sender, instance(the actual instance being saved) 
and some other args, check the docs.
- the reciever takes in the arguments in from the signal in the oder as defined
- in the above definition, we are only making use of the intance arg
'''