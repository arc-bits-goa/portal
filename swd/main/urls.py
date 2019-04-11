from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # Django Login
    url(r'^login/', views.loginform, name="login"),
    url(r'^logout/', views.logoutform, name="logout"),

    #login_success
    url(r'^accounts/profile/', views.login_success, name='login-success'),


    url(r'^project/', views.project, name="faculty"),
    url(r'^hod/$', views.hod, name="hod"),
    # url(r'^leave/', views.leave, name="leave"),
    
    url(r'^hod/([0-9]+)/$', views.hodprojectapprove, name="hodprojectapprove"),
    # url(r'^hostelsuperintendent/([0-9]+)/$', views.hostelsuperintendentdaypassapprove, name="hostelsuperintendentdaypassapprove"),
    # url(r'^student/(?P<id>\d+)/$',views.studentDetails, name="studentDetails"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
