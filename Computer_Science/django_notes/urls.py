from django.urls import path

from . import views

urlpatterns = [
    #path('django_not/',views.index1,name = 'index1'),
    path('django_notes/',views.index,name = 'index'),
    path('h/',views.hell,name = 'hell'),
]