from django.shortcuts import render, get_object_or_404
from . import models, forms

#вывод не полной информации
def book_no_full_view(request):
    book = models.Book.objects.all()
    return render(request, 'book.html', {'book': book})

#вывод полной информации по id
def book_full_view(request, id):
    book_id = get_object_or_404(models.Book, id=id)
    rating = models.Vote.objects.filter(book=book_id)
    return render(request, 'book_full.html', {
        'book_id': book_id,
        'rating': rating
    })


def add_book_view(request):
    method = request.method
    if method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'Success.html', {'form': form})

    else:
        form = forms.BookForm()

    return render(request, 'add_book.html', {'form': form})


def change_book_view(request, id):
    show_object = get_object_or_404(models.Book, id=id)
    if request.method == 'POST':
        form = forms.BookForm(instance=show_object, data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Success.html', {
                'form': form,
                'object': show_object
            })
    else:
        form = forms.BookForm(instance=show_object)

    return render(request, 'change_book.html', {
        'form': form,
        'object': show_object
    })


def delete_book_view(request, id):
    show_object = get_object_or_404(models.Book, id=id)
    show_object.delete()
    return render(request, 'Success.html', {'object': show_object})