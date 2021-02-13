# Generated by Django 3.1.5 on 2021-02-08 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chairman', '0021_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_subject', models.CharField(blank=True, max_length=30)),
                ('event_description', models.CharField(blank=True, max_length=100)),
                ('event_picture', models.FileField(default='defaultpic.png', upload_to='images/')),
                ('event_date', models.DateField(blank=True)),
                ('event_time', models.TimeField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Events',
        ),
    ]
