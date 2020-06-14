from django.contrib.auth.models import User
from django.db import models


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cards')
    date = models.DateField(auto_now_add=True)
    contents = models.TextField()
    is_required = models.BooleanField(default=False)
