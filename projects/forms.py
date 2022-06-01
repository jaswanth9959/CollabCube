from pyexpat import model
from django import forms
from django.forms import ModelForm, widgets
from django import forms
from .models import Project,Review, Resume

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','featured_image','description','demo_link','source_link',]

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
    def __init__(self, *args,**kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
        # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add Title'})
        # self.fields['description'].widget.attrs.update({'class':'input','placeholder':'Add description'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value','body']
        labels = {
            'value':'place your vote',
            'body': 'Add a comment with your vote'
        }
    def __init__(self, *args,**kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        exclude = ['owner']
        labels = {
            'name': 'Enter your name',
            'location':'Enter your address',
            'mail':'Enter your mail address',
            'mobile':'Enter your contact number',
            'social_linkedin': 'Enter your Linkedin url',
            'social_github':'Enter your Github url',
            'social_website': 'Enter your portfolio url',
            'short_intro':'Describe yourself in few words',
            'college_name':'Enter your undergrad collage name',
            'course_and_branch':'Enter your course name (ex: CSE, ECE)',
            'college_year':'Course Duration ',
            'college_percentage':'Percentage attained (ex: 85)',
            'intercollege_name':'Enter your intermediate collage name',
            'inter_course':'Duration',
            'inter_percentage':'Percentage attained (ex: 85)',
            'school_name':'Enter your school name',
            'school_year':'Duration',
            'school_percentage':'Percentage attained (ex: 85)',
            'experienceone_role':'Role of work ',
            'experienceone_duration':'Duration',
            'experienceone_company':'Employer',
            'experienceone_description':'Describe your role',
            'experiencetwo_role':'Role of work',
            'experiencetwo_duration':'Duration',
            'experiencetwo_company':'Employer',
            'experiencetwo_description':'Describe your role',
            'projectone_title':'Title of your first project',
            'projectone_description':'Describe about the project',
            'projectone_demolink':'Enter the demolink of project',
            'projecttwo_title':'Title of your second project',
            'projecttwo_description':'Describe about the project',
            'projecttwo_demolink':'Enter the demolink of project',
            'projectthree_title':'Title of your third project',
            'projectthree_description':'Describe about the project',
            'projectthree_demolink':'Enter the demolink of project',
            'certificateone_title':'Certification Name',
            'certificateone_year':'Year',
            'certificatetwo_title':'Certification Name',
            'certificatetwo_year':'Year',
            'certificatethree_title':'Certification Name',
            'certificatethree_year':'Year',
            'achievementone':'Your Achievement one',
            'achievementtwo':'Your Achievement two',
            'achievementthree':'Your Achievement three', 
            'language_one':'Language known one',
            'language_two':'Language known two',
            'language_three':'Language known three',           
        }
    def __init__(self, *args,**kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)

        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})