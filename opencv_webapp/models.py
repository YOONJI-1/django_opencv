from django.db import models

# Create your models here.
class ImageUploadModel(models.Model):
    description =models.CharField(max_length=225, blank=True)
    document = models.ImageField(upload_to='images/%y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)



    
