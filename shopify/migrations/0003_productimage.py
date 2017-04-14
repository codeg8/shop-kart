# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 06:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shopify.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopify', '0002_category_product_productcategories'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=shopify.models.upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('created_date', models.DateField()),
                ('modified_by', models.IntegerField(blank=True, null=True, unique=True)),
                ('modified_date', models.DateField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopify.Product')),
            ],
        ),
    ]