# posts/forms.py

from django import forms
from django.core.exceptions import ValidationError

from .models import Post
from .validators import validate_symbols


class PostForm(forms.ModelForm):
    memo = forms.CharField(max_length=80, validators=[validate_symbols])  # (1)

    class Meta:
        model = Post
        fields = ["title", "content"]

    def clean_title(self):  # (2)
        title = self.cleaned_data['title']  # (3)
        if '*' in title:
            raise ValidationError("*는 포함될 수 없습니다.")
        return title