from django.urls import path
from .views import upload, result, get_data



urlpatterns = [
    path('', upload, name='upload'),
    path('result/<int:image>/', result, name='result'),
    path('data/<int:image>/', get_data, name='get_data')
]