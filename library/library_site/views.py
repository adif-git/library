from django.shortcuts import render
from .models import Book, Author
from django.views import generic
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    num_books = Book.objects.count()
    num_authors = Author.objects.count()

    context = {
        'num_books':num_books,
        'num_authors':num_authors,
    }

    return render(request, 'index.html', context=context)

def Admin(request):
    pass

class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'

class AuthorUpdate(UpdateView):
    model=Author
    fields ='__all__'

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')

class BookCreate(CreateView):
    model = Book
    fields = '__all__'

class BookUpdate(UpdateView):
    model = Book
    fields ='__all__'

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')
