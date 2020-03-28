from django.contrib import admin

# Register your models here.
from .models import Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name')
    fields = [('first_name','last_name')]

admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','date_published','number_of_pages','type_of_book')
    list_filter = ('author','type_of_book')

admin.site.register(Book, BookAdmin)
