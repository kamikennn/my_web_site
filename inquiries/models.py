from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

class Inquiry(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('inquiry_detail', args=[str(self.id)])

class Comment(models.Model):
    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE, related_name='comments',)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('inquiry_list')