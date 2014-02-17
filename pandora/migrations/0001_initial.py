# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table(u'pandora_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filename', self.gf('django.db.models.fields.CharField')(unique=True, max_length=1024)),
            ('dt', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('mimetype', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('size', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal(u'pandora', ['Item'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table(u'pandora_item')


    models = {
        u'pandora.item': {
            'Meta': {'ordering': "['-dt']", 'object_name': 'Item'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'mimetype': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'size': ('django.db.models.fields.BigIntegerField', [], {})
        }
    }

    complete_apps = ['pandora']