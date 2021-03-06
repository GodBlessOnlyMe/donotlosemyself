from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from posts.validators import validate_symbols, validate_no_special_characters


class User(AbstractUser):
    nickname = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        error_messages={
            "unique": "이미 사용 중인 닉네임입니다."
        },
        validators=[validate_no_special_characters]
    )  # (1)

    def __str__(self):
        return self.email


class Post(models.Model):
    title = models.CharField(max_length=50, unique=True, error_messages={'unique': '이미 있는 제목이네요.'})
    content = models.TextField(
        validators=[
            MinLengthValidator(10, '너무 짧군요! 10자 이상 적어주세요.'),
            validate_symbols
        ])  # (1)
    dt_created = models.DateTimeField(verbose_name='Date Created', auto_now_add=True)
    dt_modified = models.DateTimeField(verbose_name='Date Modified', auto_now=True)

    def __str__(self):
        return self.title
