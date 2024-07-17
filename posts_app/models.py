from django.db import models

# Create your models here.

class Posts(models.Model):
    post_title = models.CharField(max_length=100)
    post_description = models.TextField(max_length=2500)
    post_image = models.ImageField(upload_to='images/')
    post_create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title
    
    class Meta:
        verbose_name = 'POST'
        verbose_name_plural = 'Posts'
        ordering = ['id']