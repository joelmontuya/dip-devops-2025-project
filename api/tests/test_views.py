from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Book


class BookViewTest(APITestCase):
    
    def test_response_is_correct(self):
        book = Book.objects.create(
            **{
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
                "title": book.title,
                "description": book.description,
                "author": book.author,
                "created_at": book.created_at.isoformat().replace("+00:00", "Z")               
            }
        ]

    

class HealthViewTest(APITestCase):
    
    def test_response_is_correct(self):
        url = reverse('api:health')
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        assert body['status'] == 'OK'
        assert body['status_message'] == 'Server is up and running.'
