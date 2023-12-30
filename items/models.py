from django.db import models

# Create your models here.
class Items(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/')
    is_published = models.BooleanField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Duck'
        verbose_name_plural = 'Ducks'
        ordering = ['title']
