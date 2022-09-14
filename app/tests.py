from django.test import TestCase
from .models import Book, Library


class ModelTesting(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Fire and Blood", author="J.R Martin", in_stock=10
        )
        self.library = Library.objects.create(name="Mountain Top", total_books=300)
        self.library.book.add(self.book)

    def test_book_model(self):
        new_book = self.book
        self.assertTrue(isinstance(new_book, Book))
        self.assertEqual(str(new_book.title), "Fire and Blood")
        self.assertEqual(str(self.library.name), "Mountain Top")
