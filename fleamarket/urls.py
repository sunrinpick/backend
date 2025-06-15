from django.urls import path
from .views import FleaItemView


urlpatterns = [
    path('items/', FleaItemView.as_view(), name='items'),
]