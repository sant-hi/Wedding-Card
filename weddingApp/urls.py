from django.urls import path
from weddingApp import views
urlpatterns=[
    path('index/',views.index,name='index'),

]