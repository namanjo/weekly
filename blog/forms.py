from django import forms
from blog.models import Blog, Comment
from django.contrib.auth.models import User


class BlogForm(forms.ModelForm):
    class Meta():
        model = Blog
        fields = ('title', 'cover_pic', 'text')

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author', 'comment_text')

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ('username', 'password', 'email')
