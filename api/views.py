from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookSerializer
from rest_framework import status
from .models import Book

#Create an endpoint to perform healthcheck
class HealthCheck(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'status': 'OK',
            'status_message': 'Server is up and running.'
        })
health_view = HealthCheck.as_view()

#
# Enable endpoints for /api/books
# get - retrieve all books
# post - add new book to the database
# delete - remove a book from the database
#
class BookView(APIView):
    def get(self, request, *args, **kwargs):
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        
        serializer = BookSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
    
    def delete(self, request, *args, **kwargs):
        book_id = kwargs.get('book_id')
        try: 
            book = Book.objects.get(book_id=book_id)
        except Book.DoesNotExist:
                return Response({
                    'status': status.HTTP_404_NOT_FOUND,
                    'status_message':f'Book with ID {book_id} does not exist.'
                },
                status=status.HTTP_404_NOT_FOUND)
        
        book.delete()
    
        return Response({
            'status': status.HTTP_204_NO_CONTENT,
            'status_message': 'Book was deleted successfully.'
        }, status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, *args, **kwargs):
        book_id = kwargs.get('book_id')
        data= request.data
        try:
            book = Book.objects.get(book_id=book_id)
        except Book.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'status_message': f'Book with ID {book_id} does not exist.'
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

        
book_view = BookView.as_view()

