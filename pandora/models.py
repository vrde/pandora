from django.db import models


class Item(models.Model):
    filename = models.CharField(max_length=1024, unique=True)
    dt = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=1024)
    description = models.TextField(null=True)
    mimetype = models.CharField(max_length=255)
    ip_address = models.IPAddressField()
    size = models.BigIntegerField()

    def __unicode__(self):
        return self.name

