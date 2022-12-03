from rest_framework import serializers

from weesh.weesh_item.models import Weesh


class WeeshSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weesh
        fields = "__all__"
