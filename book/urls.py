from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_no_full_view, name='book'),
    path('book/<int:id>/', views.book_full_view, name='details'),
]