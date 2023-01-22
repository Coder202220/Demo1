from . import views
from django.urls import path

urlpatterns=[
    path('',views.home,name='home'),
    path('ao/', views.arithop, name='arithop'),
    #path('contact/', views.third, name='contact'),
    #path('details/', views.fourth, name='details'),
   # path('thanks/', views.fivth, name='thanks')
]