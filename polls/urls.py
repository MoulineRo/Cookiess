from django.urls import path

from . import views

urlpatterns = [
    path(' ', views.start, name='start'),
    path('get/<int:id>/', views.get, name='get'),
    path('edit/<int:id>/', views.blog_edit, name='blog_edit'),
]
