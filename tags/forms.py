from tags.models import Tag
from django.forms import ModelForm


class TagForm(ModelForm):
    class Meta:
        model = Tag
        # exclude = ['slug', ]
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control mt-1', 'placeholder': 'Tag Name'}
        )
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control mt-1', 'placeholder': 'Tag Description'}
        )

