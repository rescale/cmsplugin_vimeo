# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Vimeo'
        db.create_table('cmsplugin_vimeo', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('video_id', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('autoplay', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('width', self.gf('django.db.models.fields.IntegerField')(default=510)),
            ('height', self.gf('django.db.models.fields.IntegerField')(default=300)),
            ('border', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('loop', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('cmsplugin_vimeo', ['Vimeo'])


    def backwards(self, orm):
        # Deleting model 'Vimeo'
        db.delete_table('cmsplugin_vimeo')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_vimeo.vimeo': {
            'Meta': {'object_name': 'Vimeo', 'db_table': "'cmsplugin_vimeo'", '_ormbases': ['cms.CMSPlugin']},
            'autoplay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'border': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '300'}),
            'loop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'video_id': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '510'})
        }
    }

    complete_apps = ['cmsplugin_vimeo']

