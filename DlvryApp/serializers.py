from .models import  Organization, Item, Pricing, SignUpModel
from rest_framework import serializers

class SignupSerializer(serializers.ModelSerializer):
    class Meta :
        model = SignUpModel
        fields = ('__all__')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUpModel
        fields = ('__all__')

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