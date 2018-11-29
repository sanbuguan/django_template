from django.shortcuts import render,redirect,render_to_response
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.http import HttpResponse

from ..setting.logconfig import *
from ..lib.testlib import *

import   django_app.db_models.test_model as test_model

