
from django.urls import path,include
from . import views

urlpatterns = [
    path('hello',views.TestFunc,name='hello'),
    path('hello1',views.TestFunc1,name='hello1'),
    path('hello2',views.TestFunc2,name='hello2'),
    path('index',views.indexFunc,name='index'),
    path('about',views.aboutFunc,name='about'),
    
]