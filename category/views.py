# For Generating URLs
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Category Objects in Django
from category.models import Category, SubCategory
from category.forms import CategoryForm, SubcategoryForm

# Custom Mixin Import
from account.mixins import SuperUserMixin


class ListViewCategory(SuperUserMixin, ListView):
    model = Category
    template_name = 'category/list.html'
    context_object_name = 'categories'


class CategoryCreateView(SuperUserMixin, SuccessMessageMixin, CreateView):
    model = Category
    template_name = 'category/form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category:list')
    extra_context = {'job': 'Create'}
    success_message = "Category created successfully."


class CategoryUpdateView(SuperUserMixin, SuccessMessageMixin, UpdateView):
    model = Category
    template_name = 'category/form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category:list')
    extra_context = {'job': 'Update'}
    success_message = "Category updated successfully."


class CategoryRemoveView(SuperUserMixin, DeleteView):
    model = Category
    template_name = 'category/remove.html'
    success_url = reverse_lazy('category:list')


# Subcategory Views
class ListViewSubCategory(SuperUserMixin, ListView):
    model = SubCategory
    template_name = 'subcategory/list.html'
    context_object_name = 'subcategories'


class SubCategoryCreateView(SuperUserMixin, SuccessMessageMixin, CreateView):
    model = SubCategory
    template_name = 'subcategory/form.html'
    form_class = SubcategoryForm
    success_url = reverse_lazy('category:subcategory_list')
    extra_context = {'job': 'Create'}
    success_message = "Sub-category created successfully."


class SubCategoryUpdateView(SuperUserMixin, SuccessMessageMixin, UpdateView):
    model = SubCategory
    template_name = 'subcategory/form.html'
    form_class = SubcategoryForm
    success_url = reverse_lazy('category:subcategory_list')
    extra_context = {'job': 'Update'}
    success_message = "Category updated successfully."


class SubCategoryRemoveView(SuperUserMixin, DeleteView):
    model = SubCategory
    template_name = 'subcategory/remove.html'
    success_url = reverse_lazy('category:subcategory_list')
    success_message = "%(name)s sub-category removed successfully."
