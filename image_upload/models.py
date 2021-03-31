from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db.models.fields.files import ImageField
from imagekit.models import ProcessedImageField
# from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, SmartResize, ResizeToFit

# def upload_to(instance, filename):
#     if(request.user):
#         username = request.user.get_username()
#     else:
#         username = 'no_user'
#     return f'media_images/{username}/{filename}'

# class Image(models.Model):
#     media_image = ImageField(upload_to='images')
#     media_image_thumbnail = ImageSpecField(source='media_image',
#                                             processors=[ResizeToFill(100, 100)],
#                                             format='JPEG',
#                                             options={'quality': 60})

# class Image(models.Model):
#     media_image = ProcessedImageField(upload_to='media_images',
#                                             processors=[ResizeToFill(100, 100)],
#                                             format='JPEG',
#                                             options={'quality': 60})
#     def get_absolute_url(self):
#         return reverse('success', kwargs={'pk': self.pk})

import os
from datetime import datetime
from uuid import uuid4

def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        timestamp = str(datetime.now().timestamp()).split('.')[0]
        if instance.user.id:
            filename = f"{timestamp}-{instance.user.id}.{ext}"
        else:
            filename = f'{timestamp}-no_user.{ext}'

        return os.path.join(path, filename)
    return wrapper

class Image(models.Model):
    media_image = ProcessedImageField(upload_to=path_and_rename('media_images'))
    user = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.DO_NOTHING)

    # def get_absolute_url(self):
    #     return reverse('success', kwargs={'pk': self.pk})
