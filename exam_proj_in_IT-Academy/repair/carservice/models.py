from django.db import models

class Employee(models.Model):

    name = models.CharField(blank=False, max_length=50)
    position = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=50, unique=True)
    photo = models.ImageField(upload_to='employee_photo')

    def __str__(self):
        return self.name



class Service(models.Model):

    name = models.CharField(blank=False, max_length=50)
    photo = models.ImageField(upload_to='service_photo')
    description = models.TextField()
    
    def __str__(self):
        return self.name