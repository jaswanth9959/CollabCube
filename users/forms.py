from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Message, Profile,Skill,Announcement,Notes
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','password1','password2']
        labels = {
            'first_name':'Name',
        }
    def __init__(self, *args,**kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','username','role','facultyid_or_studentid','short_intro','bio','profile_image','social_github','social_linkedin','social_twitter','social_website']
        labels={
            'facultyid_or_studentid':'FacultyId/StudentId',
            'social_linkedin':'Enter your linkedin url',
            'social_github':'Enter your github url',
            'social_twitter':'Enter your twitter url',
            'social_website':'Enter your portfolio url',
            
        }
    def __init__(self, *args,**kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
class SkillForm(ModelForm):
    class Meta:
        model=Skill
        fields = '__all__'
        exclude = ['owner']
    def __init__(self, *args,**kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name','email','subject','body']
    def __init__(self, *args,**kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

# class DateInput(forms.DateInput):
#     input_type= 'date'

# class TimeInput(forms.DateInput):
#     input_type= 'time'

class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = '__all__'
        exclude = ['owner']
        labels = {
            'event_date': 'Event time (YYYY-MM-DD HH:MM:SS)'
        }
    def __init__(self, *args,**kwargs):
        super(AnnouncementForm, self).__init__(*args, **kwargs)

        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'
        exclude = ['owner']
    def __init__(self, *args,**kwargs):
        super(NotesForm, self).__init__(*args, **kwargs)

        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
