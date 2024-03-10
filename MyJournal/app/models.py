from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

class Post(models.Model):
	content = models.CharField(max_length=2048)
	author = models.ForeignKey(Profile, on_delete=models.CASCADE)
	update_available = models.BooleanField(default=False)

class UpdatePost(models.Model):
	content = models.CharField(max_length=2048)
	author = models.ForeignKey(Profile, on_delete=models.CASCADE)
	original_post = models.ForeignKey(Post, on_delete=models.CASCADE)