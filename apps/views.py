from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from apps.models import Book


class HomeListView(ListView):
    queryset = Book.objects.all()
    template_name = 'main.html'
    context_object_name = 'books'

    def get_queryset(self):
        qs = super().get_queryset()
        if search := self.request.GET.get('search'):
            qs = qs.filter(name__icontains=search)
        return qs