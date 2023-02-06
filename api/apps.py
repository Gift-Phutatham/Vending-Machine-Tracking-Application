from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Configuration."""

    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "api"
