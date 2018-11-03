from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
# Create your views here.
from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

from . import models, forms

from django.contrib.auth import get_user_model
User = get_user_model()

class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ('user', 'group')

class UserPost(generic.ListView):
    model = models.Post
    template_name ='posts/user_post_list.html'

    def get_querset(self):
        try:
            self.post_user = User.object.prefetch_related('post').get(username__iexact=self.kwargs.get('username'))
        except UserDoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context

class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ('user', 'group')

    def get_querset(self):
        queryest = super().get_querset()
        return queryest.filter(user__username__iexact=self.kwargs.get('username'))

class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('message', 'group')
    model = models.Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ('user', 'group')
    seccess_url = reverse_lazy('posts:all')

    def get_querset(self):
        queryest = super().get_querset()
        return queryest.filter(user_id = self.request.user.id)

    def delete(self, *args, **kwargs):
        message.success(self.request, 'Post Deleted')
        return super().delete(*args, **kwargs)
