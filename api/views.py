from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookSerializer
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
    
        
book_view = BookView.as_view()




