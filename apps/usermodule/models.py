from django.db import models
from django.core.exceptions import ValidationError


class Address(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city



class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Card(models.Model):
    card_number = models.IntegerField(unique=True)

    def __str__(self):
        return f"Card #{self.card_number}"



class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.title} ({self.code})"



class StudentLap9(models.Model):
    name = models.CharField(max_length=100)
    card = models.OneToOneField(
        Card,
        on_delete=models.PROTECT,  
        related_name="student"
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE, 
        related_name="students"
    )
    courses = models.ManyToManyField(Course, related_name="students")


    def __str__(self):
        return self.name


class Address2(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    addresses = models.ManyToManyField(Address2)

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.title
