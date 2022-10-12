from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug>', HomeView.as_view(), name='category'),
    path('signup', signup, name='signup'),
    path('details/<slug>', ProductDetailView.as_view(), name='productdetails'),
    path('review/slug', )
]