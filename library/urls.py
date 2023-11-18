from django.urls import path
from .views import *

urlpatterns = [
    path('books/', book_list , name='book-list'),
    path('book/<int:book_id>', book_detail , name='book-detail'),
    path('book/create/', CreateBook.as_view() , name='create-book'),
    path('book/edit/<int:pk>', EditBook.as_view() , name='edit-book'),
    path('book/delete/<int:pk>', DeleteBook.as_view() , name='delete-book'),
  
]
