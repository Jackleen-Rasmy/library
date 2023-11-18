from django.shortcuts import render
from .models import * 
from django.views.generic import CreateView, UpdateView, DeleteView


def book_list(request):
    books = Book.objects.all()
    
    return render(request, 'library/book_list.html' , {'books':books})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {'book':book}
    return render(request, 'library/book_detail.html', context)


class CreateBook(CreateView):
    model = Book
    fields = '__all__'                       
    success_url = '/books/'
    
    
class EditBook(UpdateView):
    model = Book
    fields = '__all__'
    success_url = '/books/'
    template_name = 'library/book_edit.html'
    
    
class DeleteBook(DeleteView):
    model = Book
    success_url = '/books/'
    
