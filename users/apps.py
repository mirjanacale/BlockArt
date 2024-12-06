from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

def ready(self):
    """This method is called when the application is ready. 
    It imports the users.signals module to ensure that the signal handlers are connected."""
    import users.signals   # noqa: F401