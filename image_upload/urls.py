from django.urls import path
from .views import upload_view, SuccessView, SuccessLazyView


urlpatterns = [
    path('', upload_view, name='upload'),
    path('success/<int:pk>/', SuccessView.as_view(), name='success' ),
    path('success_lazy/', SuccessLazyView.as_view(), name='success_lazy')
]