from django.db import models
import uuid

# Create your models here.

class EmployeeDatabase(models.Model):
    name = models.CharField(max_length=25)
    employee_id = models.IntegerField()
    designation = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

    salaryLPA = models.IntegerField()
    
    experience_tuple = (
        ('0',"Beginner"),
        ('1',"1 year"),
        ('2',"2 years"),
        ('3',"3 years"),
        ('4',"more than 3 years")
    )

    profile_img = models.ImageField(null=True, blank=True, default='employee_logo.jpg')

    total_experience = models.CharField(max_length=30,choices=experience_tuple,null=True)

    skillset = models.ManyToManyField('SkillSet')

    created_timestamp = models.DateTimeField(auto_now_add=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.name

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
    

