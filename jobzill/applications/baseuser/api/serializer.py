from ..models import BaseUser
from django.conf import settings
from rest_framework import exceptions
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from dj_rest_auth import serializers as djserializers
from .forms import ModifiedPasswordResetForm

class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ['first_name','last_name','email','password']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = BaseUser
        fields = ['email','password']
    
    @staticmethod
    def validate_auth_user_status(user):
        if not user.is_active:
            msg = _('User account is disabled.')
            raise exceptions.ValidationError(msg)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = get_object_or_404(BaseUser,email=email, password=password)


        if not user:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        # Did we get back an active user?
        self.validate_auth_user_status(user)

        attrs['user'] = user
        return attrs

class PasswordResetSerializer(djserializers.PasswordResetSerializer):
    reset_form = None

    @property
    def password_reset_form_class(self):
        return ModifiedPasswordResetForm
        
    # def get_email_options(self):
    #     """Override this method to change default e-mail options"""
    #     return {}

    # def validate_email(self, value):
    #     # Create PasswordResetForm with the serializer
    #     self.reset_form = self.password_reset_form_class(data=self.initial_data)
    #     if not self.reset_form.is_valid():
    #         raise serializers.ValidationError(self.reset_form.errors)

    #     return value

    def save(self):
        if 'allauth' in settings.INSTALLED_APPS:
            from allauth.account.forms import default_token_generator
        else:
            from django.contrib.auth.tokens import default_token_generator

        request = self.context.get('request')
        # Set some values to trigger the send_email method.
        opts = {
            'use_https': request.is_secure(),
            'from_email': "pradippandey455@gmail.com",
            'request': request,
            'token_generator': default_token_generator,
        }

        opts.update(self.get_email_options())
        print("I am here____________________")
        self.reset_form.save(**opts)


class PasswordResetConfirmSerializer(djserializers.PasswordResetConfirmSerializer):
    """
    Serializer for confirming a password reset attempt.
    """
    # new_password1 = serializers.CharField(max_length=128)
    # new_password2 = serializers.CharField(max_length=128)
    # uid = serializers.CharField()
    # token = serializers.CharField()

    # set_password_form_class = SetPasswordForm

    # _errors = {}
    # user = None
    # set_password_form = None

    # def custom_validation(self, attrs):
    #     pass

    # def validate(self, attrs):
    #     if 'allauth' in settings.INSTALLED_APPS:
    #         from allauth.account.forms import default_token_generator
    #         from allauth.account.utils import url_str_to_user_pk as uid_decoder
    #     else:
    #         from django.contrib.auth.tokens import default_token_generator
    #         from django.utils.http import urlsafe_base64_decode as uid_decoder

    #     # Decode the uidb64 (allauth use base36) to uid to get User object
    #     try:
    #         uid = force_str(uid_decoder(attrs['uid']))
    #         self.user = UserModel._default_manager.get(pk=uid)
    #     except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
    #         raise ValidationError({'uid': ['Invalid value']})

    #     if not default_token_generator.check_token(self.user, attrs['token']):
    #         raise ValidationError({'token': ['Invalid value']})

    #     self.custom_validation(attrs)
    #     # Construct SetPasswordForm instance
    #     self.set_password_form = self.set_password_form_class(
    #         user=self.user, data=attrs,
    #     )
    #     if not self.set_password_form.is_valid():
    #         raise serializers.ValidationError(self.set_password_form.errors)

    #     return attrs

    # def save(self):
    #     return self.set_password_form.save()

    # pass

    # def save(self, request):
    #     self.cleaned_data = self.get_cleaned_data()
    #     user = BaseUser(self.cleaned_data)
    #     return self.create(self.validated_data)