from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView, DetailView, FormView, View

from .forms import ImageUploadForm
from .models import Image

def upload_view(request, *args, **kwargs):
    # form = ImageUploadForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            obj = form.save(commit=False)
            image = request.FILES.get('media_image')
            
            if request.user: 
                obj.user = request.user
            else:
                obj.user = ''

            obj.save()
            print(obj.pk)
            return redirect(reverse('success', kwargs={'pk': obj.pk}))
    else:
        form = ImageUploadForm()

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