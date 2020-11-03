from django.shortcuts import render
from django.views.generic import CreateView ,ListView
from .models import Review
from django.urls import reverse

# Create your views here.
class ReviewListView(ListView):
    model = Review
    template_name = 'home/home.html'
    context_object_name = 'review'
    ordering = ['-date_posted']


class ReviewCreateView(CreateView):
    model = Review
    fields = ['name', 'content']

    def get_success_url(self):
        return reverse('home')
