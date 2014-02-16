from django.conf import settings
from ajaxuploader.backends.local import LocalUploadBackend
import django.dispatch

upload_complete = django.dispatch.Signal(providing_args=['request', 'filename'])


class SignalBasedLocalUploadBackend(LocalUploadBackend):

    UPLOAD_DIR = settings.UPLOAD_PATH


    def upload_complete(self, request, filename, *args, **kwargs):
        upload_complete.send(sender=self, request=request, filename=filename)

