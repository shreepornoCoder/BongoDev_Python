from rest_framework import serializers
from . models import User, Address

class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ['created_at', 'updated_at']

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email'] 