from django.shortcuts import render
from django.views.generic import CreateView, DetailView

from .models import Image


class UploadView(CreateView):
    model = Image
    fields = [
        'media_image',
    ]
    template_name = 'image_upload/upload_form.html'

class SuccessView(DetailView):
    model = Image
    template_name = 'image_upload/image_upload_detail.html'