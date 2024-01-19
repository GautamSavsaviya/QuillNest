from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField
from base.models import BaseModel


# Create your models here.
class Blog(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='blogs/images', default='default-blog.png')
    slug = models.SlugField(max_length=100, null=True, blank=True, unique=True)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> CharField:
        return self.title

