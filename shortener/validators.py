from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validate_url(value):
    url_validator = URLValidator()
    invalid1 = False
    invalid2 = False
    try:
        url_validator(value)
    except:
        invalid1 = True

    try:
        url = "https://" + value
    except:
        invalid2 = True

    if not invalid1 and invalid2 :
        raise ValidationError("invalid url")
    return value

def validate_dot_com(value):
    if 'com' not in value:
        raise ValidationError("this is not a url")
    return value
