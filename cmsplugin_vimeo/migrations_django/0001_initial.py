# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vimeo',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('video_id', models.CharField(max_length=60, verbose_name='video id')),
                ('autoplay', models.BooleanField(default=False, verbose_name='autoplay')),
                ('width', models.IntegerField(default=425, verbose_name='width')),
                ('height', models.IntegerField(default=344, verbose_name='height')),
                ('border', models.BooleanField(default=False, verbose_name='border')),
                ('loop', models.BooleanField(default=False, verbose_name='loop')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
