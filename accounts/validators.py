from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_tg(tg):
    if tg[0] != '@':
        raise ValidationError(
            _('Telegram must starts with @')
        )
