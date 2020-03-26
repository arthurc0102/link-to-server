from rest_framework import serializers

from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = (
            'id',
            'code',
            'url',
            'create_at',
        )


class LinkAnonymousSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = (
            'code',
            'url',
        )
        read_only_fields = (
            'code',
        )
