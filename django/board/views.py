from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Post


class IndexView(CreateView):
    success_url = reverse_lazy('index')
    template_name = 'board/index.html'
    model = Post
    fields = ['author', 'message']

    def get_context_data(self, **kwargs):
        kwargs['posts_list'] = Post.objects.order_by('-created_at')
        return super().get_context_data(**kwargs)
