# Generated by Django 3.1.5 on 2021-02-05 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0026_complaint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='citizen_id',
        ),
        migrations.DeleteModel(
            name='citizen',
        ),
        migrations.DeleteModel(
            name='complaint',
        ),
    ]
