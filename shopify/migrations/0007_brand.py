# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-12 06:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0006_remove_product_brands'),
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopify.Product')),
            ],
        ),
    ]
