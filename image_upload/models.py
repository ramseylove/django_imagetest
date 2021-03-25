from django.db import models
from django.urls import reverse
# from django.contrib.auth import get_user_model
from django.db.models.fields.files import ImageField
from imagekit.models import ProcessedImageField
# from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# class Image(models.Model):
#     media_image = ImageField(upload_to='images')
#     media_image_thumbnail = ImageSpecField(source='media_image',
#                                             processors=[ResizeToFill(100, 100)],
#                                             format='JPEG',
#                                             options={'quality': 60})

class Image(models.Model):
    media_image = ProcessedImageField(upload_to='media_images',
                                            processors=[ResizeToFill(100, 100)],
                                            format='JPEG',
                                            options={'quality': 60})
    def get_absolute_url(self):
        return reverse('success', kwargs={'pk': self.pk})

