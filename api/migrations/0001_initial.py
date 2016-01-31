# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('address', models.CharField(max_length=200)),
                ('contact_person', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('designation', models.CharField(max_length=100)),
                ('min_salary', models.IntegerField()),
                ('max_salary', models.IntegerField()),
                ('shift_timing', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('branches', models.ManyToManyField(related_name='jobs', to='api.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='JobBranches',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(related_name='branches', to='api.Branch')),
                ('job', models.ForeignKey(related_name='jobs', to='api.Job')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('locations', models.ManyToManyField(null=True, to='api.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sectors', models.ManyToManyField(null=True, to='api.Sector')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='sector',
            field=models.ForeignKey(related_name='jobs', to='api.Sector'),
        ),
        migrations.AddField(
            model_name='branch',
            name='company',
            field=models.ForeignKey(related_name='branches', to='api.Company'),
        ),
        migrations.AddField(
            model_name='branch',
            name='location',
            field=models.ForeignKey(related_name='branches', to='api.Location'),
        ),
    ]
