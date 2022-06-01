# Generated by Django 4.0.1 on 2022-03-01 10:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_announcement_announce_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='announce_image',
            field=models.ImageField(blank=True, default='announcement.png', null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('branch', models.CharField(choices=[('cse', ' CSE'), ('ece', 'ECE')], max_length=30)),
                ('semister', models.CharField(choices=[('1st', ' 1st Semister'), ('2nd', '2nd Semister')], max_length=30)),
                ('subject', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('notesfile', models.FileField(upload_to='')),
                ('filetype', models.CharField(choices=[('docx', 'docx'), ('pdf', 'pdf'), ('ppt', 'PPT')], max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]