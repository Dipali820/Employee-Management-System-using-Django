from django.db import models

# Student model
class StudentModel(models.Model):
    rollo = models.IntegerField()
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    fee = models.FloatField()

    class Meta:
        db_table = 'studentmodel'
        managed = True
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

# Employee model
class EmpModel(models.Model):
    empid = models.IntegerField()
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    salary = models.FloatField()

    class Meta:
        db_table = 'EmpModel'
        managed = True
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
