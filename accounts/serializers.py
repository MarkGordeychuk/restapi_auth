from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from phonenumber_field.serializerfields import PhoneNumberField

from .models import User


class LoginSerializer(serializers.Serializer):
    login = serializers.CharField(
        label=_("Login"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    # token = serializers.CharField(
    #     label=_("Token"),
    #     read_only=True
    # )

    def validate(self, attrs):
        login = attrs.get('login')
        password = attrs.get('password')

        if login and password:
            user = authenticate(request=self.context.get('request'),
                                login=login, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "login" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    # token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'login', 'password', 'phone', 'name', 'birth', 'tg', 'email',)
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
            'tg': {'required': False},
            'email': {'required': False},
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
#
#
# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('login', 'password',)
#         extra_kwargs = {'password': {'write_only': True}}
