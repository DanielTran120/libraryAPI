from django.test import TestCase
from django.urls import reverse
# Create your tests here.
from .models import Book

class BookTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        cls.book=Book.objects.create(
            title ="a good title",
            subtitle="good subtitle",
            author= "Daniel",
            isbn = "123456789"
        )

    def test_book_contents(self):
        self.assertEqual(self.book.title, "a good title")
        self.assertEqual(self.book.subtitle, "good subtitle")
        self.assertEqual(self.book.author, "Daniel")
        self.assertEqual(self.book.isbn, "123456789")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "good subtitle")
        self.assertTemplateUsed(response, "books/book_list.html")