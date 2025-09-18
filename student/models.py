from django.db import models
from django.contrib import admin
# Create your models here.
class StudentDetail(models.Model):
    name = models.CharField(max_length=100, help_text="Enter the name")
    dob = models.DateField(help_text="Enter Date of Birth")
    age = models.IntegerField(help_text="Age between 18 to 23")
    course_name = models.CharField(max_length=100, help_text="")
    department = models.CharField(max_length=100, help_text="Enter the Department")
    reg_no = models.IntegerField(help_text="Enter Register No")

class StudentDetailAdmin(admin.ModelAdmin):
    list_display = ('name','dob','age','course_name','department','reg_no')