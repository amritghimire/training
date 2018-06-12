from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    title = models.CharField(max_length=225,null=True)
    text = models.TextField(null=True,blank=True)
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(blank=True,null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.title