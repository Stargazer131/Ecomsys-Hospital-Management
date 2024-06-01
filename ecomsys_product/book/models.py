from django.db import models
from django.urls import reverse
from product.models import random_id, Product


# Create your models here.
class Book(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    genres = models.ManyToManyField('Genre', through='BookGenre')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, related_name='books')


    class Meta:
        db_table = 'books'
        ordering = ['product__name']


    def __str__(self):
        return self.product.name
    
    
class Genre(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)


    class Meta:
        db_table = 'genres'
        ordering = ['name']


    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(Genre)
        super().save(*args, **kwargs)

        
class BookGenre(models.Model):
    id = models.BigIntegerField(primary_key=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(BookGenre)
        super().save(*args, **kwargs)
        
        
    class Meta:
        db_table = 'book_genres'
    

class Author(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    birthday = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ])


    class Meta: 
        db_table = 'authors'
        ordering = ['name']


    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(Author)
        super().save(*args, **kwargs)
    
    
class Publisher(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, null=True, blank=True)


    class Meta:
        db_table = 'publishers'
        ordering = ['name']


    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(Publisher)
        super().save(*args, **kwargs)
    