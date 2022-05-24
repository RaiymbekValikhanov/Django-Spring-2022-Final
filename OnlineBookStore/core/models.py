from django.db import models
from _auth.models import UserProfile

# Create your models here.
class BookJournalBase(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    description = models.TextField()
    created_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=255)

    def __str__(self):
        return super().__str__() + f', {self.genre}'

class Journal(BookJournalBase):
    class Type(models.TextChoices):
        Bullet = 'bullet'
        Food = 'food'
        Travel = 'travel'
        Sport = 'sport'

    type = models.CharField(max_length=255, choices=Type.choices)
    publisher = models.ForeignKey(UserProfile, on_delete=models.PROTECT, related_name='journals', null=True, blank=True)

    def __str__(self):
        return super().__str__() + f', {self.type}, {self.publisher.user.username}'


