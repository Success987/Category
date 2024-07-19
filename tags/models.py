from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(validators=[MinLengthValidator(20), ])
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tags'
        verbose_name = 'Tag'
        verbose_name_plural = "Tags"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save()
