# Generated by Django 2.0 on 2018-07-09 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happy', '0013_healthy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='healthy',
            old_name='type',
            new_name='hlytype',
        ),
    ]