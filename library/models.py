from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()

    def __str__(self):
        return self.first_name + " " + self.last_name

class Genre(models.Model):
    genre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.genre

class Publication(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.TextField(max_length=250)
    isbn = models.CharField(max_length=13)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " by " + str(self.author) + " (ISBN: " + self.isbn + ")"

class Book(models.Model):
    book = models.ForeignKey(Publication, on_delete=models.CASCADE)
    imprint = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('Available', ('Available to borrow')),
        ('Borrowed', ('Borrowed by someone')),
        ('Archived', ('Archived - no longer available'))
    ]
    status = models.CharField(max_length=32, choices=STATUS_CHOICES)

    def __str__(self):
        return str(self.book) + " / Added: " + str(self.date_added) + " / Status: " + self.status