# Generated by Django 3.1.5 on 2021-02-04 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0015_law'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='law',
            name='date_time',
        ),
    ]