from django.contrib import admin

from weesh.organization.models import Address, Organization, OrganizationCategory

# Register your models here.
admin.site.register(Organization)
admin.site.register(OrganizationCategory)
admin.site.register(Address)
