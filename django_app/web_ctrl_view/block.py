from django.shortcuts import render,redirect,render_to_response
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.http import HttpResponse

from ..django_app.setting.xxxxx import *
from ..django_app.lib.testlib import *

import   django_app.db_models.test_model as test_model


def block(request):
    # return HttpResponse('This is cook_sess page index...')
    app_list=test.xxxxxxx.objects.all().values()
    context={}
    context['app_list']=xxxxx
    context['web_title']='应用列表'
    return render(request, 'django_app/some_html/block.html', context)
