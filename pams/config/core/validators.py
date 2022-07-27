from django.core.exceptions import ValidationError


def validate_alphabet(value: str):
    if not value.isalpha():
        raise ValidationError(
            "%(value) is not a valid alphabet",
        )
