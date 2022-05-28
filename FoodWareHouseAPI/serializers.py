from rest_framework import serializers
from . models import foods

class foodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = foods
        fields = ('Mfd_id', 'Name', 'unitPrice', 'unitStock' )