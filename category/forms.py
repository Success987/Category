from django.forms import ModelForm
from category.models import Category, SubCategory


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control mt-1'}
        )
        self.fields['image'].widget.attrs.update(
            {'class': 'form-control mt-1'}
        )


class SubcategoryForm(ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name', 'image', 'description', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control mt-1'}
        )
        self.fields['image'].widget.attrs.update(
            {'class': 'form-control mt-1'}
        )
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please add a proper description.'}
        )
        self.fields['category'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please add a proper description.'}
        )