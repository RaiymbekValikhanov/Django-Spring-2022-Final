from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    class Role(models.IntegerChoices):
        Guest = 1
        SuperAdmin = 2

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    role = models.IntegerField(choices=Role.choices)

    def __str__(self):
        return f'{self.user.username}, {self.role}'
