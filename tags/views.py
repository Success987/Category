from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from tags.models import Tag
from tags.forms import TagForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy


# @login_required(login_url='accounts:login')
# def home(request):
#     return HttpResponse("Hello, world. You're Logged In.")


class TagListView(LoginRequiredMixin, ListView):
    model = Tag
    login_url = 'account:login'
    template_name = 'tag/list.html'
    context_object_name = 'tags'


class TagCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Tag
    template_name = 'tag/form.html'
    form_class = TagForm
    success_url = reverse_lazy('tag:list')
    extra_context = {'job': 'Create'}
    success_message = "Tag created successfully."


class TagUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Tag
    template_name = 'tag/form.html'
    form_class = TagForm
    success_url = reverse_lazy('tag:list')
    extra_context = {'job': 'Update'}
    success_message = "Tag updated successfully."


class TagRemoveView(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = 'category/remove.html'
    success_url = reverse_lazy('tag:list')