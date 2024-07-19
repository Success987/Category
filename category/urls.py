from django.urls import path
from category.views import (
    ListViewCategory, CategoryCreateView, CategoryUpdateView, CategoryRemoveView,
    ListViewSubCategory, SubCategoryCreateView, SubCategoryUpdateView, SubCategoryRemoveView
)

app_name = 'category'

urlpatterns = [
    path('category/', ListViewCategory.as_view(), name='list'),
    path('category/create/', CategoryCreateView.as_view(), name='create'),
    path('category/update/<slug:slug>', CategoryUpdateView.as_view(), name='update'),
    path('category/remove/<slug:slug>', CategoryRemoveView.as_view(), name='remove'),

    path('subcategory/', ListViewSubCategory.as_view(), name='subcategory_list'),
    path('subcategory/create/', SubCategoryCreateView.as_view(), name='subcategory_create'),
    path('subcategory/update/<slug:slug>', SubCategoryUpdateView.as_view(), name='subcategory_update'),
    path('subcategory/remove/<slug:slug>', SubCategoryRemoveView.as_view(), name='subcategory_remove'),
]
