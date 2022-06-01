# Generated by Django 4.0.1 on 2022-04-12 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='certificateone_description',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='certificatetwo_description',
        ),
        migrations.AddField(
            model_name='resume',
            name='achievementone',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='achievementthree',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='achievementtwo',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='certificatethree_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='certificatethree_year',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
