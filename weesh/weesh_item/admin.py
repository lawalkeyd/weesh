from django.contrib import admin

from weesh.weesh_item.models import FulfilWeesh, Weesh

# Register your models here.
admin.site.register(Weesh)
admin.site.register(FulfilWeesh)
