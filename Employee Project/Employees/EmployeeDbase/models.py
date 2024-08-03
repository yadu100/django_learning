from django.db import models
import uuid

from django.contrib.auth.models import User

# Create your models here.

class EmployeeDatabase(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)


    name = models.CharField(max_length=25, null=True, blank=True)
    employee_id = models.IntegerField(null=True, blank=True)
    designation = models.CharField(max_length=50, null=True, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)

    salaryLPA = models.IntegerField(null=True, blank=True)
    
    experience_tuple = (
        ('0',"Beginner"),
        ('1',"1 year"),
        ('2',"2 years"),
        ('3',"3 years"),
        ('4',"more than 3 years")
    )

    profile_img = models.ImageField(null=True, blank=True, default='employee_logo.jpg')

    total_experience = models.CharField(max_length=30,choices=experience_tuple, null=True, blank=True)

    skillset = models.ManyToManyField('SkillSet', null=True, blank=True)

    created_timestamp = models.DateTimeField(auto_now_add=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['created_timestamp']

class SkillSet(models.Model):
    Programming_language = models.CharField(max_length=50)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.Programming_language
    
class EmployeeReview(models.Model):
    nameofEmployee = models.ForeignKey('EmployeeDatabase',on_delete=models.CASCADE)
    review_text = models.TextField(default="nil", max_length=2000)

    def __str__(self) -> str:
        return self.nameofEmployee.name
    

