from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class Chapter(models.Model):
    chapter=models.CharField(max_length=50)
    
    title=models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True) # new
    description=RichTextUploadingField(max_length=15000)
    
#     creation_date=models.DateTimeField()

    def __str__(self):
        return self.chapter

    def get_absolute_url(self):
        return reverse('chapter_detail', kwargs={'slug': self.slug}) 