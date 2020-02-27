from django import forms
from blog.models import Blog, Comment


class BlogForm(forms.ModelForm):
    class Meta():
        model = Blog
        fields = ('title', 'cover_pic', 'text')

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author', 'comment_text')
