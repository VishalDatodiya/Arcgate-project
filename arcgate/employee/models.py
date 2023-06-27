from django.db import models


class Profile(models.Model):
    profile_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.profile_name

class Employee(models.Model):
    name = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    city = models.CharField(max_length=200, null=True)
    age = models.IntegerField(default=0, null=True)
    salary = models.IntegerField(default=20000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
