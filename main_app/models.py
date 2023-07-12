from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class StatusChoices(models.TextChoices):
    active = 'active', _('Active')
    contingent = 'contingent', _('Contingent')
    under_contract = 'under contract', _('Under Contract')
    pending = 'pending', _('Pending')

class Showing(models.Model):
    address = models.CharField(max_length=100, help_text='(Street, City, State, Zip)')
    preferred_time = models.CharField(max_length=100)
    other_availability = models.CharField(max_length=100)
    status = models.CharField(max_length=15, choices=StatusChoices.choices)
    notes = models.TextField()
        # add user_id FK column
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.address} {self.user} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'showing_id': self.id})