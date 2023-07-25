from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='post', default='fail')
    tags = models.ManyToManyField(Tag, null=True, blank=True)

    def __str__(self):
        return self.title

