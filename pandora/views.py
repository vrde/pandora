from django.shortcuts import render
from django.middleware.csrf import get_token
from ajaxuploader.views import AjaxFileUploader
from pandora.backends import SignalBasedLocalUploadBackend

from pandora.models import Item


def home(request):
    return render(request, 'pandora/home.html', {
            'items': Item.objects.all(),
            'csrf_token': get_token(request)
        })


import_uploader = AjaxFileUploader(SignalBasedLocalUploadBackend)

