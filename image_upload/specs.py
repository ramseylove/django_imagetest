from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFit

class ShrinkImage(ImageSpec):
    processors = [ResizeToFit(1000,)]
    format = 'JPEG'
    options = {'quality': 90}

register.generator('image_upload:shrinkImage', ShrinkImage)