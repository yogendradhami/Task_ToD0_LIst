from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=90,null=False)
    description=models.TextField(null=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='todo',null=True,blank=True,)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_complete =models.BooleanField(default=False)


    def __str__(self):
        return f'{self.user.first_name}- {self.title}' 
    
    class Meta:
        ordering= ['is_complete']
