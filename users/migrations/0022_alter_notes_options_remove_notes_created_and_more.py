# Generated by Django 4.0.1 on 2022-03-01 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_alter_notes_uploaded_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'ordering': ['-uploaded_on']},
        ),
        migrations.RemoveField(
            model_name='notes',
            name='created',
        ),
        migrations.AlterField(
            model_name='notes',
            name='uploaded_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]