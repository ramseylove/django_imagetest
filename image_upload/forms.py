from django import forms
from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFit

from .specs import ShrinkImage
from .models import Image

class ImageUploadForm(forms.ModelForm):

    media_image = ProcessedImageField(spec_id='image_upload:shrinkImage',
                                        processors=[ResizeToFit(1000)],
                                        format='JPEG',
                                        options={'quality': 90})
    class Meta:
        model = Image
        fields = ['media_image']

    