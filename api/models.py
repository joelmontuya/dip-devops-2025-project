from django.db import models

# Create a class Book
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, null=True, blank=True)
    published_date = models.DateField(null=True, blank=True) #YYYY-mm-dd format 
    created_at = models.DateTimeField(auto_now_add=True)