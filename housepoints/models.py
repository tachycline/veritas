from django.db import models
from django.conf import settings

# Create your models here.

class House(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    grade=models.IntegerField(default=3)
    house = models.ForeignKey(House)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

        
class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class FacStaffType(models.Model):
    type_name = models.CharField(max_length=200)
    point_total = models.IntegerField(default=5000)
    def __str__(self):
        return "{} ({})".format(self.type_name, self.point_total)
    
class FacStaff(models.Model):
    name = models.CharField(max_length=200)
    house_affiliation = models.ForeignKey(House, blank=True, null=True)
    facstafftype = models.ForeignKey(FacStaffType)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    
    
class Award(models.Model):
    student = models.ForeignKey(Student, blank=True, null=True)
    house = models.ForeignKey(House)
    amount = models.IntegerField(default=0)
    category = models.ForeignKey(Category, blank=True, null=True)
    date_awarded = models.DateTimeField()
    # awarded_by needs to be a user

    def __str__(self):
        return "{0:%d} to {1:%s} ({2:%s})".format(self.amount, self.house, self.student)
    
