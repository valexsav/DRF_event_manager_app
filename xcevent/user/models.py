from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    GUEST = 'GUEST'
    ORGANIZER = 'ORGANIZER'
    PARTICIPANT = 'PARTICIPANT'
    role_choices = [
        (GUEST, 'Guest'),
        (ORGANIZER, 'Organizer'),
        (PARTICIPANT, 'Participant'),
    ]

    role = models.CharField(
        max_length=11,
        choices=role_choices,
        default=GUEST,
    )

    def __str__(self):
        return self.username