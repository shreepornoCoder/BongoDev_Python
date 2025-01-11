from rest_framework import serializers
from . models import User, Address

class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ['created_at', 'updated_at']

class UserSerializers(serializers.ModelSerializer):
    addresses = AddressSerializers(many=True, read_only=True)
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'password', 'address', 'addresses']

        extra_kwargs = {"password":{"write_only":True, 'required':True}}# Extra security - Password won't be able to read from api

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)

        user.save()

        return user
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
