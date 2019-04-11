from django.db import models
from django.contrib.auth.models import User
import os
import re
from django.utils import timezone
DEPARTMENTS = (
    ('CHE', 'CHE'),
    ('EEE', 'EEE'),
    ('ECE', 'EEE'),
    ('CS', 'CS'),
    ('MECH', 'MECH'),
    ('INSTR', 'INSTR'),
    ('MATH','MATH'),
    ('PHY','PHY'),
    ('CHEM','CHEM'),
    ('ECON','ECON'),
    ('BIO','BIO'),
    ('HSS','HSS'),
    ('BITS','BITS')
)
COURSE_CODES=(
    ('F266','F266'),
    ('F366','F366'), 
    ('F367','F367'),
    ('F376','F376'), 
    ('F377','F377'), 
    ('F491','F491'),
    ('F382','F382'),  
)
class Hod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    department = models.CharField(max_length=5, choices=DEPARTMENTS, null=True, blank=True)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    studentname = models.CharField(max_length = 100, null= True, blank = False,verbose_name = 'Student Name')
    studentId = models.CharField(max_length = 13, null= True, blank = False,verbose_name = 'Student ID')
    title = models.CharField(max_length = 200, null=True,blank =False, verbose_name = 'Project Title')
    department = models.CharField(max_length=5, choices=DEPARTMENTS, null=True, blank=False,verbose_name = 'Department Code')
    courseCode = models.CharField(max_length=30, choices=COURSE_CODES, null=True, blank=False,verbose_name = 'Course Code')
    faculty = models.ForeignKey('Faculty', on_delete = models.CASCADE,verbose_name = 'Faculty')
    approved = models.BooleanField(default=0, blank=True,verbose_name = 'Approved')
    disapproved = models.BooleanField(default=0, blank=True)
    inprocess = models.BooleanField(default=1, blank=True)
    def __str__(self):
        return self.faculty.name + ' '+ self.studentname + ' ' + str(self.id)


