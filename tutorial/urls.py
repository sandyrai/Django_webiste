
from django.urls import path
from  tutorial import views


urlpatterns = [

     path('',views.home , name='home'),
     path('tutorial/<slug:slug>/', views.chapter_detail, name='chapter_detail'),
     path('About', views.about , name='about'),

]

