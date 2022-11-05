from django.db import models
from django.utils import timezone

# Create your models here.
from weesh.organization.models import Organization
from weesh.utils.choices import WeeshCategoryChoices


class Weesh(models.Model):
    name = models.CharField(max_length=50)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    category = models.PositiveSmallIntegerField(choices=WeeshCategoryChoices.CATEGORIES)
