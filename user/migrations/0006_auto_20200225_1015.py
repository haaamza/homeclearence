# Generated by Django 3.0.3 on 2020-02-25 10:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0005_auto_20200225_1014'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserItems',
            new_name='UserItem',
        ),
    ]