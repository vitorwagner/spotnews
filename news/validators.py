from django.core.exceptions import ValidationError


def validate_title_word_count(value):
    if len(value.split()) < 2:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")
