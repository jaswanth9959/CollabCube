# Generated by Django 4.0.1 on 2022-03-01 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_remove_announcement_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='featured_image',
            field=models.ImageField(default='announcement.png', null=True, upload_to=''),
        ),
    ]