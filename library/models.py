from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from djangoratings.fields import RatingField
from django.core.validators import MaxValueValidator, MinValueValidator
'''
Author
    name 
    birth_date 
    biography 

Book
    title 
    author 
    publication_date 
    price 

Review:
    book 
    reviewer_name
    content 
    rating(1:5)  
----------------------------  
ToDo:
    - github repo with project 
    - design models 
    - Generate CRUD for Books


'''

class Author(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    birth_date = models.DateField(blank=True,null=True)
    biography = models.TextField(max_length=10000,blank=True,null=True)
    
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_book')
    publication_date = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=6, decimal_places=2,blank=True,null=True)
    
    def __str__(self):
        return self.title
    
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_review')
    reviewer_name = models.ForeignKey(User, related_name='reviewed_by', on_delete=models.CASCADE)
    content = models.TextField(max_length=10000,blank=True,null=True)
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    # rating = RatingField(range=5)
    
    
    
