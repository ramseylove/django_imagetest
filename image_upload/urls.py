from django.urls import path
from .views import UploadView, SuccessView


urlpatterns = [
    path('', UploadView.as_view(), name='upload'),
    path('success/<int:pk>/', SuccessView.as_view(), name='success' )
]