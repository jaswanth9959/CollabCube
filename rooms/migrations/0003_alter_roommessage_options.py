# Generated by Django 4.0.1 on 2022-06-01 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_room_password'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roommessage',
            options={'ordering': ['updated', 'created']},
        ),
    ]
