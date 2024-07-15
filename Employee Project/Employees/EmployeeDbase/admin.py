from django.contrib import admin

from .models import EmployeeDatabase, SkillSet, EmployeeReview

# Register your models here.

admin.site.register(EmployeeDatabase)
admin.site.register(SkillSet)
admin.site.register(EmployeeReview)