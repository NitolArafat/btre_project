# Generated by Django 3.0.6 on 2020-06-04 16:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 4, 21, 37, 11, 94542)),
        ),
    ]