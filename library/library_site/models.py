from django.db import models
from django.urls import reverse

class Book(models.Model):
    BOOK_TYPES = (
        ('Novel','Novel'),
        ('Documentation','Documentation'),
        ('Other','Other'),
    )

    title = models.CharField(blank=False, max_length=255, null = True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, blank=False, null=True, max_length=255)
    date_published = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    number_of_pages = models.IntegerField(blank=True, null=True)
    type_of_book = models.CharField(max_length=255,choices=BOOK_TYPES, null=True, blank=True)

    class Meta:
        ordering = ["title"]

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=False)
    last_name = models.CharField(max_length=100, null=True, blank=False)

    class Meta:
        ordering = ['first_name','last_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
