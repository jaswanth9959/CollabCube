from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model= Room
        fields = '__all__'
        exclude = ['host','topic']

    def __init__(self, *args,**kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)

        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})