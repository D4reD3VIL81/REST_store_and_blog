from django.db import models
from account.models import AccountModel
from django.conf import settings
from django.urls import reverse


# Create your models

class Post(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.title})
    