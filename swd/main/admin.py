from django.contrib import admin
from main.models import *
from django.utils.html import format_html
import urllib
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User, Group

models = [Hod,Faculty,Student]
admin.site.register(models)
admin.site.unregister(Group)
