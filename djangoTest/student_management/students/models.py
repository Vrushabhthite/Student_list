from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    course = models.CharField(max_length=50)
    # images=models.ImageField(upload_to='media')
    images = models.ImageField(upload_to='students/', null=True, blank=True)



    def __str__(self):
        return self.name
