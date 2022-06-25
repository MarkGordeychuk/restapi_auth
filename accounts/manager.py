from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, login, phone, birth, password, **extra_fields):
        if not login:
            raise ValueError(_('The Login must be set'))
        if not phone:
            raise ValueError(_('The Phone number must be set'))
        if not birth:
            raise ValueError(_('The Birthday must be set'))

        if 'email' in extra_fields:
            extra_fields['email'] = self.normalize_email(extra_fields['email'])

        user = self.model(login=login, phone=phone, birth=birth, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, login, phone, birth, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(login, phone, birth, password, **extra_fields)
