from django.core.validators import MinValueValidator, MaxValueValidator


def max_min(min_value, max_value):
    return [MinValueValidator(min_value), MaxValueValidator(max_value)]
