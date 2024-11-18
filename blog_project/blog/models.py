from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Post(models.Model):
        author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  
        title = models.CharField(max_length=200)
        content = RichTextField()
        image = models.ImageField(upload_to='post_images/', blank=True, null=True)
        category = models.DateTimeField(auto_now=True)

        def __str__(self):
             return self.title
        

class Comment(models.Model):
     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
     author = models.ForeignKey(User, on_delete=models.CASCADE)
     content = models.TextField()
     parent = models.ForeignKey('self',null=True, blank=True, on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return f'Comment by{self.author} on {self.post}'
     
     

          
