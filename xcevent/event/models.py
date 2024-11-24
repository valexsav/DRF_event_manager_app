from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    total_tickets = models.IntegerField()
    available_tickets = models.IntegerField()
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=40)
    organizer = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'ORGANIZER'},
        related_name='organized_events',
        )
    participants = models.ManyToManyField(
        'user.User',
        related_name='events_participated',
        blank=True,
    )

    def __str__(self):
        return self.title