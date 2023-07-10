from django.db import models
from django.urls import reverse


# Create your models here.
class StatusChoices(models.TextChoices):
    active = 'active'
    contingent = 'contingent'
    under_contract = 'under contract'
    pending = 'pending'

class Showing(models.Model):
    address = models.CharField(max_length=100)
    preferred_time = models.CharField(max_length=100)
    other_availability = models.CharField(max_length=100)
    status = models.CharField(max_length=15, choices=StatusChoices.choices)
    notes = models.TextField()

# review code below
    def __str__(self):
        return f'{self.address} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'showing_id': self.id})