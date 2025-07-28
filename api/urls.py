from django.urls import path
from .views import book_view, health_view

app_name = 'api'

urlpatterns = [
    path('', health_view, name='health'),
    path('books/', book_view, name='books'),
    path('books/<int:book_id>/', book_view, name='books-delete')
]