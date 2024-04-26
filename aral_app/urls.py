from django.urls import path
from .views import home, add_contact, about, portfolio_detail, blog_detail, custom_404
import re

urlpatterns = [
    path('', home, name='home'),
    path('add-contact/', add_contact, name='add_contact'),
    path('about/', about, name='about'),
    path('portfolio/<int:pk>/', portfolio_detail, name='portfolio_detail'),
    path('blog/<int:pk>/', blog_detail, name='blog_detail'),
    path('404/', custom_404, name='404')
]