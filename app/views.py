from django.views.generic import View
from django.shortcuts import render
from .models import Post


class IndexView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.all()
        return render(request, 'app/index.html', {
            'post_data': post_data,
        })
