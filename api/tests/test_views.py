from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Book


class BookViewTest(APITestCase):
    
    def test_response_is_correct(self):
        book = Book.objects.create(
            **{
                "book_id": 1,
                "title": "test_title",
                "description": "test_description",
                "author": "test_author"
            }
        )

        url = reverse('api:books')
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        assert body== [          
            {
                'book_id':book.book_id,
                "title": book.title,
                "description": book.description,
                "author": book.author,
                "created_at": book.created_at.isoformat().replace("+00:00", "Z")               
            }
        ]

class BookDeleteTestCase(APITestCase):
    def setUp(self):
        # Create a test book
        self.book = Book.objects.create(
            title="title",
            description="To be deleted.",
            author="author"
        )
        self.url = reverse('api:books-delete', kwargs={'book_id': self.book.book_id})

    def test_delete_book_success(self):
        response = self.client.delete(self.url)

        # Test if deletion returns 204
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check the book is deleted
        self.assertEqual(Book.objects.count(), 0)

    def test_delete_nonexistent_book(self):
        non_existent_url = reverse('api:books-delete', kwargs={'book_id': 999})
        response = self.client.delete(non_existent_url)

        # Test if 404 is returned
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('status_message', response.data)
 

class HealthViewTest(APITestCase):
    
    def test_response_is_correct(self):
        url = reverse('api:health')
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        assert body['status'] == 'OK'
        assert body['status_message'] == 'Server is up and running.'
