from rest_framework import serializers

from pathology.models import Plant


class PlantSerializer(serializers.ModelSerializer):
    """
    Serializer for News of users
    """

    class Meta:
        """
        Meta class for NewsSerializer
        """

        model = Plant
        exclude = [
          
        ]
