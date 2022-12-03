from django.db import models
from django.utils import timezone

# Create your models here.
from weesh.organization.models import Organization
from weesh.users.models import User
from weesh.utils.choices import WeeshCategoryChoices


class Weesh(models.Model):
    name = models.CharField(max_length=50)
    category = models.PositiveSmallIntegerField(choices=WeeshCategoryChoices.CATEGORIES)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.IntegerField(default=1)
    quantity_value = models.DecimalField(
        null=True, blank=True, max_digits=12, decimal_places=2
    )
    value = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    fulfiled = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class FulfilWeesh(models.Model):
    weesh = models.ForeignKey(Weesh, on_delete=models.CASCADE)
    amount = models.DecimalField(null=True, blank=True, max_digits=12, decimal_places=2)
    quantity = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.weesh
