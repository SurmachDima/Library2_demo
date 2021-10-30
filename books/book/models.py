from django.db import models
from django.urls import reverse


class Genre(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название книги')
    author = models.ForeignKey('Author', verbose_name='Автор', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=2000, verbose_name='Описание')
    isbn = models.CharField('ISBN', max_length=13)
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    year_published = models.DateField(max_length=4, verbose_name='Год публикации')
    pages = models.CharField(max_length=6, verbose_name='Количество страниц')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='Автор')

    def __str__(self):
        return self.name

    def absolute_url(self):
        return reverse('author-detail', args=[(self.id)])