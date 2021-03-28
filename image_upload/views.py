from django.shortcuts import render

from django.views.generic import CreateView, DetailView, FormView, View

from .forms import ImageUploadForm
from .models import Image

def upload_view(request, *args, **kwargs):
    form = ImageUploadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # print(form.cleaned_data)
        obj = form.save(commit=False)
        image = request.FILES.get('media_image')
        
        if request.user: 
            obj.user = request.user
        else:
            obj.user = ''
            
        print(image.content_type)
        print(image.name)
        print(image.size)
        print(image.file)
        # print(image.path)
        print(image.image)
        new_image = image._set_name = 'image_likeness.png'

        obj.save()

    return render(request, "image_upload/upload_form.html", {'form': form})

# class UploadView(FormView):
#     model = Image
#     form_class = ImageUploadForm
#     template_name = 'image_upload/upload_form.html'

#     success_url = '/success_lazy/'

#     def form_valid(self, form):

#         return super().form_valid(form)

class SuccessView(DetailView):
    model = Image
    template_name = 'image_upload/image_upload_detail.html'

class SuccessLazyView(View):
    model = Image
    template_name = 'image_upload/success_lazy.html'