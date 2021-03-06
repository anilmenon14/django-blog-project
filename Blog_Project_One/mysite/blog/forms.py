from django import forms
from blog.models import Post,Comment,UserProfileInfo
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')
        # widgets have to be inside Meta class . Note intendation
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')
        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')
        widgets = {
            'username':forms.TextInput(attrs={'class':'techfont'}),
            'email':forms.TextInput(attrs={'class':'techfont'}),
            'password':forms.TextInput(attrs={'class':'techfont'})
        }


class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
        widgets = {
            'portfolio_site':forms.TextInput(attrs={'class':'techfont'})
        }
