from django import forms
from django.forms import widgets
from django.forms.widgets import Textarea
from django.forms import ModelForm      
from .models import Post
class PostForm(ModelForm):
    '''PostTitle = forms.CharField(label='What your recipe is called', max_length=255)
    PostDesc = forms.CharField(widget=forms.Textarea,label= "A short description of your recipe to display")
    PostContent = forms.CharField(widget=forms.Textarea,label= "Your Recipe here")
    Image = forms.CloudinaryField('image')
    '''
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('user','userName')
        labels = {
        "postTitle": "What Your Recipe is called",
        "postDesc": "A short description of your recipe to display",
        "postContent":"Your Recipe",
        "image":"Image of your dish"
        }
        widgets = {
            'postDesc': Textarea(attrs={'cols': 40, 'rows': 5}),
        }

