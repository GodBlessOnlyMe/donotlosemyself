# posts/forms.py

from django import forms
from django.core.exceptions import ValidationError

from .models import User, Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                    'class': 'title',
                    'placeholder': '제목을 입력하세요'}),
            'content': forms.Textarea(attrs={
                    'placeholder': '내용을 입력하세요'})}

    def clean_title(self):
        title = self.cleaned_data['title']
        if '*' in title:
            raise ValidationError('* 는 포함될 수 없습니다.')
        return title


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname"]

    def signup(self, request, user):
        user.nickname = self.cleaned_data["nickname"]  # (1)
        user.save()
