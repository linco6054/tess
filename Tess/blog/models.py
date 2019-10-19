from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Admin_Post(models.Model):
    title= models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    content =models.TextField()
    document = models.ImageField(upload_to='images/')
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})
