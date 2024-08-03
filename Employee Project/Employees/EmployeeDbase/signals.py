from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import EmployeeDatabase


from django.core.mail import send_mail
from django.conf import settings


def signalEmployeeCreation(sender, instance, created, **kwargs):
    if created:
        User = instance
        new_employee = EmployeeDatabase.objects.create(
            name = User.first_name,

        )

    # subject = "Registration Successful"
    # body = "Hi, your registration is successful. welcome to employee database"

    # send_mail(
    #     subject,
    #     body,
    #     settings.EMAIL_HOST_USER,
    #     [User.email],
    #     fail_silently=False
    # )
    


post_save.connect(signalEmployeeCreation, sender=User)



