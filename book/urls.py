from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_no_full_view, name='book'),
    path('book/<int:id>/', views.book_full_view, name='details'),
    path('book/<int:id>/change/', views.change_book_view, name='change'),
    path('book/<int:id>/delete/', views.delete_book_view, name='delete'),
    path('add-book/', views.add_book_view, name='add'),
]