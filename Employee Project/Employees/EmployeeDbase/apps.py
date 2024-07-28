from django.apps import AppConfig


class EmployeedbaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'EmployeeDbase'

    def ready(self) -> None:
        import EmployeeDbase.signals