from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'cart']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['cart']
    
    def update(self, instance, validated_data):
        print("\n\n instance \n\n")
        print(instance)
        print(validated_data)
        instance.cart = validated_data['cart']
        instance.save()
        return instance
    
    # def update(self, instance, validated_data):
    #     instance.cart = validated_data

    #     instance.save()
    #     return instance 