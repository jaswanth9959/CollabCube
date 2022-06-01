from django.db import models
import uuid
from users.models import Profile
# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(Profile, null = True, blank= True, on_delete= models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank= True)
    featured_image = models.ImageField(null=True, blank= True, default="default.jpg")
    demo_link = models.CharField(max_length=2000,null=True, blank= True)
    source_link = models.CharField(max_length=2000,null=True, blank= True)
    tags = models.ManyToManyField('Tag',blank=True)
    vote_total = models.IntegerField(blank=True,null= True, default= 0)
    vote_ratio = models.IntegerField(blank=True,null= True, default= 0)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,editable=False, primary_key=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-vote_ratio','-vote_total']

    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url
    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset

    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()
        ratio = (upVotes/totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_ratio= ratio
        self.save()


class Review(models.Model):
    VOTE_TYPE = (
        ('up','Up Vote'),
        ('down','Down Vote')
    )
    owner = models.ForeignKey(Profile, null = True, on_delete= models.CASCADE)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    body = models.TextField(null=True, blank= True)
    value = models.CharField(max_length=200,choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,editable=False, primary_key=True)

    class Meta:
        unique_together = [['owner','project']]
    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=200)    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,editable=False, primary_key=True)

    def __str__(self):
        return self.name

class Resume(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    social_linkedin = models.CharField(max_length=200,null=True,blank=True)
    social_github = models.CharField(max_length=200,null=True,blank=True)
    social_website = models.CharField(max_length=200,null=True,blank=True)
    short_intro = models.TextField(max_length=800)
    college_name = models.CharField(max_length=200)
    course_and_branch = models.CharField(max_length=300)
    college_year = models.CharField(max_length=100)
    college_percentage = models.CharField(max_length=100)
    intercollege_name = models.CharField(max_length=200)
    inter_course = models.CharField(max_length=300)
    inter_year = models.CharField(max_length=100)
    inter_percentage = models.CharField(max_length=100)
    school_name = models.CharField(max_length=200)
    school_year = models.CharField(max_length=100)
    school_percentage = models.CharField(max_length=100)
    skill_one = models.CharField(max_length=200,null=True,blank=True)
    skill_two = models.CharField(max_length=200,null=True,blank=True)
    skill_three = models.CharField(max_length=200,null=True,blank=True)
    skill_four = models.CharField(max_length=200,null=True,blank=True)
    skill_five = models.CharField(max_length=200,null=True,blank=True)
    skill_six = models.CharField(max_length=200,null=True,blank=True)
    experienceone_role = models.CharField(max_length=200,null=True,blank=True)
    experienceone_duration = models.CharField(max_length=200,null=True,blank=True)
    experienceone_company = models.CharField(max_length=200,null=True,blank=True)
    experienceone_description = models.TextField(null=True,blank=True)
    experiencetwo_role = models.CharField(max_length=200,null=True,blank=True)
    experiencetwo_duration = models.CharField(max_length=200,null=True,blank=True)
    experiencetwo_company = models.CharField(max_length=200,null=True,blank=True)
    experiencetwo_description = models.TextField(null=True,blank=True)
    projectone_title = models.CharField(max_length=200,null=True,blank=True)
    projectone_description = models.TextField(null=True,blank=True)
    projectone_demolink = models.CharField(max_length=200,null=True,blank=True)
    projecttwo_title = models.CharField(max_length=200,null=True,blank=True)
    projecttwo_description = models.TextField(null=True,blank=True)
    projecttwo_demolink = models.CharField(max_length=200,null=True,blank=True)
    projectthree_title = models.CharField(max_length=200,null=True,blank=True)
    projectthree_description = models.TextField(null=True,blank=True)
    projectthree_demolink = models.CharField(max_length=200,null=True,blank=True)
    certificateone_title = models.CharField(max_length=200,null=True,blank=True)
    certificateone_year = models.CharField(max_length=20,null=True,blank=True)
    certificatetwo_title = models.CharField(max_length=200,null=True,blank=True)
    certificatetwo_year = models.CharField(max_length=20,null=True,blank=True)
    certificatethree_title = models.CharField(max_length=200,null=True,blank=True)
    certificatethree_year = models.CharField(max_length=20,null=True,blank=True)
    achievementone = models.CharField(max_length=500,null=True,blank=True)
    achievementtwo = models.CharField(max_length=500,null=True,blank=True)
    achievementthree = models.CharField(max_length=500,null=True,blank=True)
    language_one = models.CharField(max_length=100,null=True,blank=True)
    language_two = models.CharField(max_length=100,null=True,blank=True)
    language_three = models.CharField(max_length=100,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self):
        return str(self.name)