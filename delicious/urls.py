from django.urls import path
from . views import homeview,aboutView,blogView,receipeView,contactView,blog_details
urlpatterns = [
    path('',homeview,name='home'),
    path('aboutView/',aboutView,name='aboutView'),
    path('blogView/',blogView,name='blogView'),
    path('blogdetails/<int:id>/',blog_details,name='blog_details'),
    path('receipeView/',receipeView,name='receipeView'),
    path('contactView/',contactView,name='contactView'),
]