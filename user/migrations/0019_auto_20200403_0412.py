# Generated by Django 3.0.3 on 2020-04-03 04:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_item_buynow'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='bidding_end_data',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
