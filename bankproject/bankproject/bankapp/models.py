from django.db import models

# Create your models here.
class District(models.Model):
    name=models.CharField(max_length=250,unique=True)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name=models.CharField(max_length=250,unique=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Account(models.Model):
    name=models.CharField(max_length=250,unique=True)

    def __str__(self):
        return self.name

class Materials(models.Model):
    name=models.CharField(max_length=250,unique=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name=models.CharField(max_length=250)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.BooleanField()
    phone=models.IntegerField()
    email=models.EmailField()
    district=models.ForeignKey(District, on_delete=models.CASCADE)
    branch=models.ForeignKey(Branch, on_delete=models.CASCADE)
    account=models.ForeignKey(Account,on_delete=models.CASCADE)
    materials=models.ForeignKey(Materials,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Login(models.Model):
    username=models.CharField(max_length=250,unique=True)
    password=models.CharField(max_length=250)
    objects = models.Manager()
    def __str__(self):
        return self.name

class Register(models.Model):
    username = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.name
