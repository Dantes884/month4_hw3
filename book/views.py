from django.shortcuts import render, get_object_or_404
from . import models

#вывод не полной информации
def book_no_full_view(request):
    book = models.Book.objects.all()
    return render(request, 'book.html', {'book': book})

#вывод полной информации по id
def book_full_view(request, id):
    book_id = get_object_or_404(models.Book, id=id)
    return render(request, 'book_full.html', {'book_id': book_id})