from django.urls import path
from . views import homeview,aboutView,blogView,receipeView,contactView
urlpatterns = [
    path('',homeview,name='home'),
    path('aboutView/',aboutView,name='aboutView'),
    path('blogView/',blogView,name='blogView'),
    path('receipeView/',receipeView,name='receipeView'),
    path('contactView/',contactView,name='contactView'),
]