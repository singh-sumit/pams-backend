from django.db import models


class LowercaseEmailField(models.EmailField):
    """Overrides EmailField to make email address lowercase."""

    def pre_save(self, model_instance, add):
        value = super().pre_save(model_instance, add)
        return value.lower()
