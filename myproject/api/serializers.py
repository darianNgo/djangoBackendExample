# create model serializers because the response object cannot
# natively handle complex data types such as django model instances 
from rest_framework import serializers
from base.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'