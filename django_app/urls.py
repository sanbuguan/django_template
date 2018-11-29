from django.urls import path,re_path
from django.contrib.auth.decorators import login_required

from django_app.web_ctl_view import django_app



urlpatterns = [
    path('', django_app.index, name='index'),
    path('block', django_app.index, name='block')
]