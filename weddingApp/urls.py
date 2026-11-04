from django.urls import path
from weddingApp import views
urlpatterns=[
    path('',views.index,name='index'),

]