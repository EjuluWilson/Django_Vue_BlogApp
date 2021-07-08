

from .views import printText

from django.urls import path

urlpatterns = [

    path('', printText),

]
