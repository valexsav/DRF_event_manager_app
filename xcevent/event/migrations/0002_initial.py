# Generated by Django 5.1.3 on 2024-11-24 12:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(limit_choices_to={'role': 'ORGANIZER'}, on_delete=django.db.models.deletion.CASCADE, related_name='organized_events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='events_participated', to=settings.AUTH_USER_MODEL),
        ),
    ]
