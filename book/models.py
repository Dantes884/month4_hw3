from django.db import models

class Book(models.Model):


    DEFAULT_CHOICES = (
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
        ('1', '1'),
    )


    GENRE = (
        ('HORROR', 'HORROR'),
        ('COMEDY', 'COMEDY'),
        ('FANTASY', 'FANTASY'),
        ('THRILLER', 'THRILLER'),
        ('ROMAN', 'ROMAN'),
        ('DETECTIVE', 'DETECTIVE'),
        ('ADVENTURE', 'ADVENTURE'),
    )


    title = models.CharField('Название книги', max_length=100)
    author = models.CharField('Автор книги', max_length=100)
    description = models.TextField('Описание книги')
    image = models.ImageField('Картинка', upload_to='')
    quantity = models.PositiveIntegerField('Количество страниц')
    genre = models.CharField('Жанр', max_length=100, choices=GENRE)
    link = models.URLField('Ссылка на книгу')
    price = models.PositiveIntegerField('Цена')
    mass = models.PositiveIntegerField('Масса книги в граммах')
    age_limit = models.PositiveIntegerField('Возрастное ограничение')
    rating = models.CharField('Рейтинг', max_length=100, choices=DEFAULT_CHOICES, null=True)
    created_dates = models.DateTimeField(auto_now_add=True, null=True)
    updated_dates = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return self.title


class Vote(models.Model):
    value = models.SmallIntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    voted_on = models.DateTimeField(auto_now=True)