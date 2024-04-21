from django.urls import path
from . views import homeview,aboutView,blogView,receipeView,contactView,blog_details,receipeViewdetails,searchView
urlpatterns = [
    path('',homeview,name='home'),
    path('aboutView/',aboutView,name='aboutView'),
    path('blogView/',blogView,name='blogView'),
    path('blogdetails/<int:id>/',blog_details,name='blog_details'),
    # path('recipe_create/',recipe_blog_create,name='recipe_blog_create'),
    path('receipeView/',receipeView,name='receipeView'),
    path('receipeView/<int:id>',receipeViewdetails,name='receipeViewdetails'),
    path('contactView/',contactView,name='contactView'),
    path('search/',searchView,name='search'),
]