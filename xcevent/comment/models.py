from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Comment(models.Model):
    text = models.TextField()
    event = models.ForeignKey(
        'event.Event',
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='comments',
    )
    rating = models.FloatField(
        validators=[
            MinValueValidator(0.1),
            MaxValueValidator(5.0)
        ],
    )
