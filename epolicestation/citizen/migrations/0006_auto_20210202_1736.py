# Generated by Django 3.1.5 on 2021-02-02 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0005_citizen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.DeleteModel(
            name='citizen',
        ),
    ]
