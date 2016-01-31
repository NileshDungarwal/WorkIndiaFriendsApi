# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_job_branches'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobbranches',
            name='branch',
            field=models.ForeignKey(related_name='jobs', to='api.Branch'),
        ),
        migrations.AlterField(
            model_name='jobbranches',
            name='job',
            field=models.ForeignKey(related_name='branches', to='api.Job'),
        ),
    ]
