from datetime import date

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_tg(tg):
    if tg[0] != '@':
        raise ValidationError(
            _('Telegram must starts with @')
        )


def validate_birth(birth):
    diff_years = date.today().year - birth.year
    if diff_years < 18 \
            or diff_years == 18 and (birth.month > date.today().month or
                                     birth.month == date.today().month and birth.day > date.today().day):
        raise ValidationError(
            _('User must be of legal age')
        )
