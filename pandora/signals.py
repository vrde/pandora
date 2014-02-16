from pandora.backends import upload_complete
from django.dispatch import receiver
from pandora.utils import get_client_ip
from pandora import models
import mimetypes
from django.conf import settings
import os
import re

def guess_mimetype(url):
    type, encoding = mimetypes.guess_type(url, False)

    if type:
        return type.split('/')[0]

    return 'unknown'


def get_size(url):
    return os.stat(url).st_size


def get_name(url):
    return re.sub(ur'[\W_]', u' ', os.path.splitext(url)[0], 0, re.UNICODE)


@receiver(upload_complete)
def update_database_on_upload(sender, request, filename, *args, **kwargs):
    models.Item.objects.create(
        filename=filename,
        mimetype=guess_mimetype(filename),
        size=get_size(os.path.join(settings.UPLOAD_DIR, filename)),
        name=get_name(filename),
        ip_address=get_client_ip(request))

