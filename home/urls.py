from django.urls import path
from . import views
from .views import ReviewListView, ReviewCreateView

urlpatterns = [
    path('', ReviewListView.as_view(), name='home'),
    path('add_review', ReviewCreateView.as_view(), name='add_review'),
]