from django import forms
from imagekit.forms import ProcessedImageField
from .models import Image

class ImageUploadForm(forms.ModelForm):

    def upload_to(instance, filename):
        if(request.user):
            username = request.user.get_username()
        else:
            username = 'no_user'
        return f'media_images/{username}/{filename}'

    media_image = ProcessedImageField(upload_to=upload_to,
                                            processors=[ResizeToFit(1000)],
                                            format='JPEG',
                                            options={'quality': 90})
    class Meta:
        model = Image
        fields = ['media_image']

    