from .models import *
from import_export import resources, fields
from import_export.fields import Field

class ProjectResource(resources.ModelResource):
    class Meta:
        model = Project
        fields = ('faculty__name','studentId', 'studentname', 'department', 'courseCode','title','approved')
        export_order = ('faculty__name','studentId', 'studentname', 'department', 'courseCode','title','approved')
        verbose_name = True