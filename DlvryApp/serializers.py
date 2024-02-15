from .models import Organization, Item, Pricing
from rest_framework import serializers

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta :
        model = Organization
        fields = ('__all__')
        
class ItemSerializer(serializers.ModelSerializer):
    class Meta :
        model = Item
        fields = ('__all__')
        
class PricingSerializer(serializers.ModelSerializer):
    class Meta :
        model = Pricing
        fields = ('__all__')