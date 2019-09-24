from django.conf import settings
from django.db import models
from django.utils import timezone


# Define the Post Model(s) for our blog uwu
class Post(models.Model):
    #Info/properties needed to create the post and associate fields
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # Publish Method to actually make the post
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # a dunder method? does this just override the builtin string's method?
    def __str__(self):
        return self.title