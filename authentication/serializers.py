from rest_framework import serializers
from rest_framework.authentication import get_user_model

User=get_user_model()

class UserSerializer(serializers.ModelSerializer):
    id= serializers.IntegerField(read_only=True)
    password=serializers.CharField(write_only=True)
    confirm_password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','username','password','confirm_password']
        
        
    def validate(self, attrs):
        if attrs.get('password')!=attrs.get('confirm_password'):
            raise serializers.ValidationError("Password and Confirm Password does not match")
        
        return attrs
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('confirm_password')  # Remove confirm_password from validated_data

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    
class UserLoginSerializer(serializers.ModelSerializer):
    id= serializers.IntegerField(read_only=True)
    username=serializers.CharField(max_length=255)
    password=serializers.CharField(write_only=True)
    token=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=['id','username','password','token']