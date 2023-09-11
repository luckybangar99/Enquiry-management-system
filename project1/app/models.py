from django.db import models


class UserDataBase(models.Model):
    Fname=models.CharField(max_length=50,blank=False)
    Lname=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Contact=models.IntegerField()
    Password=models.CharField(max_length=50)
    Cpass=models.CharField(max_length=50)


class AdminDataBase(models.Model):
    Fname=models.CharField(max_length=50,blank=False)
    Lname=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Contact=models.IntegerField()
    Password=models.CharField(max_length=50)
    Cpass=models.CharField(max_length=50)

class QueryDataBase(models.Model):
    Name=models.CharField(max_length=50,blank=False)
    Email=models.EmailField(max_length=50)
    Contact=models.CharField(max_length=50)
    Query=models.CharField(max_length=50)