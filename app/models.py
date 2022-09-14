from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    in_stock = models.IntegerField()

    # def remaining_stock(self):
    #     library = Library.objects.filter(book=self)
    #     return library.total_books - self.in_stock

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=100)
    book = models.ManyToManyField(Book)
    total_books = models.IntegerField()

    def __str__(self):
        return self.name
