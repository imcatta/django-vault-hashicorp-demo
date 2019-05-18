from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone


class Post(models.Model):
    author = models.CharField(max_length=100, null=False, blank=False, validators=[
                              MinLengthValidator(3)])
    message = models.CharField(max_length=240, null=False, blank=False)
    created_at = models.DateTimeField(
        null=False, blank=False, default=timezone.now)
