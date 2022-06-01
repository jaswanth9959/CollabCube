import email
from operator import pos
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
import uuid

from django.db.models.signals import post_save, post_delete

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, null=True,blank= True)
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(unique=True,max_length=300,null=True)
    username = models.CharField(max_length=200,unique=True,null=True)
    ROLE_TYPE =(
        ('faculty','Faculty'),
        ('student','Student')
    )
    role = models.CharField(max_length=200,choices=ROLE_TYPE,null=True)  
    facultyid_or_studentid = models.CharField(max_length=200,unique=True,null=True)  
    short_intro = models.CharField(max_length=200,null=True)
    bio = models.TextField(blank=True, null = True)
    profile_image= models.ImageField(default= 'profiles/male.png',null=True, upload_to ='profiles/')
    social_github = models.CharField(max_length=200,null=True,blank=True)
    social_linkedin = models.CharField(max_length=200,null=True,blank=True)
    social_website = models.CharField(max_length=200,null=True,blank=True)
    social_twitter = models.CharField(max_length=200,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ['-created']
    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(null=True,blank=True) 
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self):
        return str(self.name)



class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True,blank=True)
    recipient = models.ForeignKey(Profile,on_delete=models.SET_NULL, null=True,blank=True, related_name="messages")
    name = models.CharField(max_length=200, null=True,blank=True)
    email = models.CharField(max_length=200, null=True,blank=True)
    subject = models.CharField(max_length=200, null=True,blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null = True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self):
        return str(self.subject)
    
    class Meta:
        ordering = ['is_read','-created']


class Announcement(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=500,null=True,blank=True)
    event_date = models.DateTimeField(auto_now=False,auto_now_add=False,blank=True,null=True)
    description = models.TextField(null=True,blank=True)  
    announce_image = models.ImageField(null=True, blank= True, default="announcement.png")
    featured_link = models.CharField(max_length=200,null=True,blank=True)    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['created']


class Notes(models.Model):

    

    FilE_TYPE = (
        ('docx','docx'),
        ('pdf','pdf'),
        ('ppt','PPT')
    )

    Sem = (
        ('1st',' 1st Semister'),
        ('2nd','2nd Semister'),
        ('3rd','3rd Semister'),
        ('4th','4th Semister'),
        ('5th','5th Semister'),
        ('6th','6th Semister'),
        ('7th','7th Semister'),
        ('8th','8th Semister'),
    )

    Sem1 = (
        ('CSE',' cse'),
        ('ECE','ece'),
        ('EEE','eee'),
        ('CIVIL','civil'),
        ('MECH','mech')

    )
    

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True, blank=True)
    uploaded_on = models.DateField(auto_now_add=True)
    branch = models.CharField(max_length=30, choices=Sem1)
    semister =models.CharField(max_length=30,choices=Sem)
    subject = models.CharField(max_length=100)
    topic =models.CharField(max_length=100)
    notesfile = models.FileField()
    filetype = models.CharField(max_length=30,choices=FilE_TYPE)
    description = models.CharField(max_length=100)
    # created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self):
        return str(self.topic)

    class Meta:
        ordering = ['-uploaded_on']