from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# from rest_framework.authtoken.models import Token
from phonenumber_field.modelfields import PhoneNumberField


from .manager import UserManager
from .validators import validate_tg, validate_birth


class User(AbstractBaseUser, PermissionsMixin):
    login_validator = UnicodeUsernameValidator()

    phone = PhoneNumberField(unique=True)
    login = models.CharField(
        _("login"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[login_validator],
    )
    name = models.CharField(_("name"), max_length=150)
    birth = models.DateField(_("birthday"), validators=[validate_birth])
    tg = models.CharField(_("telegram"), max_length=64, blank=True, validators=[validate_tg])
    email = models.EmailField(_("email address"), blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['phone', 'name', 'birth']

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return f"Login: {self.login}, Phone: {self.phone}, Name: {self.name}, Birthday: {self.birth}"

    # @property
    # def token(self):
    #     return Token.objects.get_or_create(user=self)[0].key
