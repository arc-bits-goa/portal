from django import forms
from .models import Project
from django.forms.widgets import *
from django.utils.translation import ugettext_lazy as _
from datetime import date, datetime
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

class ProjectForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(ProjectForm, self).clean()
        return cleaned_data
    # courseCode = forms.ChoiceField(choices=COURSE_CODES,required = True, help_text="F266/F366/F367/F376/F377/F491")

    class Meta:
        model = Project
        fields = ['studentname','studentId','title','department','courseCode']
        exclude = ['faculty','approved', 'disapproved', 'inprocess', ]
        widgets = {
            'department': forms.TextInput(attrs={'class': 'validate'}),
            'courseCode': forms.TextInput(attrs={'class': 'validate'}),
            'title': forms.Textarea(attrs={'class': 'materialize-textarea'}),

        }
        labels = {
            'studentname': _('Student Name'),
            'studentId': _('Student ID'),
            'department': _('Department code'),
            'courseCode': _('Course Code'),
            'title': _('Project Title'),

        }



# class ProjsectForm(forms.ModelForm):
#     studentID = forms.CharField(label='Student ID Number', widget=forms.Textarea)
#     studentName = forms.CharField(label='Student Name', widget=forms.Textarea)
#     projectTitle = forms.CharField(label='Proect Title', widget=forms.Textarea)



# class printBonafideForm(forms.Form):
#     text = forms.CharField(required=True, label='Body Text', widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))

# class DayPassForm(forms.ModelForm):
#     date = forms.CharField(label='Date', widget=forms.TextInput(attrs={'class': 'datepicker'}))
#     time = forms.CharField(label='Out Time', widget=forms.TextInput(attrs={'class': 'timepicker'}))
#     intime = forms.CharField(label='In Time', widget=forms.TextInput(attrs={'class': 'timepicker'}))
#     def clean(self):
#         cleaned_data = super(DayPassForm, self).clean()
#         date = datetime.strptime(cleaned_data['date'], '%d %B, %Y').date()
#         time = datetime.strptime(cleaned_data['time'], '%H:%M').time()
#         intime = datetime.strptime(cleaned_data['intime'], '%H:%M').time()
#         date_time_start = datetime.combine(date, time)
#         if datetime.now() >= date_time_start:
#             self.add_error('date', "Daypass cannot be issued before the present date and time")
#         if (date_time_start-datetime.now()).days>2:
#             self.add_error('date', "Can apply for daypass within 2 days")
#         return cleaned_data

#     class Meta:
#         model = DayPass
#         exclude = ['student', 'approvedBy',
#                     'approved', 'comment', 'disapproved', 'inprocess', 'dateTime','inTime']
#         widgets = {
#             'reason': forms.Textarea(attrs={'class': 'materialize-textarea'}),
#             'corrAddress': forms.Textarea(attrs={'class': 'materialize-textarea validate'}),
#         }
#         labels = {
#             'corrAddress': _(" Location you're visiting "),
            
#         }
        
