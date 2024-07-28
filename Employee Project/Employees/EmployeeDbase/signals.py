from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import EmployeeDatabase

def signalEmployeeCreation(sender, instance, created, **kwargs):
    User = instance
    new_employee = EmployeeDatabase.objects.create(
        name = User.username,

    )

post_save.connect(signalEmployeeCreation, sender=User)



