from django.shortcuts import render
from django.middleware.csrf import get_token
from django.shortcuts import render_to_response
from django.template import RequestContext

from ajaxuploader.views import AjaxFileUploader



def home(request):
    return render(request, 'pandora/home.html', { 'csrf_token': get_token(request) })


import_uploader = AjaxFileUploader()
