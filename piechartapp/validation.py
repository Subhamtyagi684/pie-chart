from django.core.exceptions import ValidationError
import re


def validate_title(value):
    pattern = r'[a-zA-Z ]+'
    if re.fullmatch(pattern,str(value)):
        return value
    else:
        raise ValidationError('Please enter valid title')

        