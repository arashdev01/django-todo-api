from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        validators=[validate_password]  # اعتبارسنجی رمز عبور Django
    )
    
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        label='تکرار رمز عبور'
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password2')
        read_only_fields = ('id',)
        extra_kwargs = {
            'username': {
                'validators': [UniqueValidator(queryset=User.objects.all())]
            }
        }

    def validate(self, attrs):
        """بررسی تطابق دو رمز عبور"""
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({
                "password": "رمزهای عبور مطابقت ندارند."
            })
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user