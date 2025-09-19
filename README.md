# Ex02 Django ORM Web Application
## Date: 19.09.2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 5 Car 

## PROGRAM
~~~

model.py
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

admin.py
from django.contrib import admin
from.models import StudentDetail, StudentDetailAdmin
# Register your models here.
admin.site.register(StudentDetail, StudentDetailAdmin)

~~~
## OUTPUT
![alt text](<Screenshot 2025-09-18 215440.png>) ![alt text](<Screenshot 2025-09-18 214810.png>) ![alt text](<Screenshot 2025-09-18 214906.png>) ![alt text](<Screenshot 2025-09-18 215109.png>)

## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
