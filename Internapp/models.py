from django.db import models

# Create your models here.

class department(models.Model):
    course = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    slug = models.CharField(max_length=20)

    def __str__(self):
        return self.course

class Intern(models.Model):
    department = models.ForeignKey(department , on_delete= models.CASCADE)
    name = models.CharField(max_length=35)
    created_on = models.DateTimeField(auto_now_add=True)
    ends_on = models.DateField()
    phone_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name