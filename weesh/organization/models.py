from django.db import models
from django.utils import timezone

# Create your models here.


class Address(models.Model):
    address_line_one = models.CharField(max_length=50)
    address_line_two = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=10, default="Nigeria")
    city = models.CharField(max_length=20, default="Ibadan")
    state = models.CharField(max_length=20, default="Oyo")


class OrganizationCategory(models.Model):
    category = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    address = models


class Documents(models.Model):
    certificate_of_incorporation = models.FileField()


class Organization(models.Model):
    name = models.CharField(max_length=34)
    category = models.ForeignKey(OrganizationCategory, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    documents = models.ForeignKey(
        Documents, on_delete=models.CASCADE, null=True, blank=True
    )
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)
