from rest_framework import serializers
# from .models import User
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields =['id', 'username', 'email', 'password', 'password2']
        extra_kwargs={'password': {'write_only':True}}

    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        
        if len(password) <= 5:
            raise serializers.ValidationError("Weak Password")
    
        return attrs
       
        

    def create(self, validated_data):
        # Remove 'password2' from validated_data
        validated_data.pop('password2', None)
        user=User.objects.create_user(**validated_data)
        return user


class changePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, max_length=255, style={'input_type': 'password'}, write_only=True)
    new_password = serializers.CharField(required=True, max_length=255, style={'input_type': 'password'}, write_only=True)
    confirm_password = serializers.CharField(required=True, max_length=255, style={'input_type': 'password'}, write_only=True)

    def validate(self, attrs):
        old_password = attrs.get('old_password')
        new_password = attrs.get('new_password')
        confirm_password = attrs.get('confirm_password')
        user = self.context.get('user')

        if not user.check_password(old_password):
            raise serializers.ValidationError('Old password is incorrect')

        if new_password != confirm_password:
            raise serializers.ValidationError("New Password and Confirm Password don't match")

        if len(new_password) <= 7:
            raise serializers.ValidationError("Weak Password")
        
        user.set_password(new_password)
        user.save()
        return attrs



class resetPasswordEmailSerializer(serializers.Serializer):
    email=serializers.EmailField(required=True, max_length=50, style={'input_type':'email'}, write_only=True)

        

