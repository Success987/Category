from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator, FileExtensionValidator

# For Admin Panel Interface
from django.utils.html import format_html
from django.utils.functional import cached_property


# Create your views here.
class Category(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(3), ], unique=True)
    slug = models.SlugField(validators=[MinLengthValidator(3), ])
    image = models.ImageField(
        upload_to='image/category/', validators=[
            FileExtensionValidator(
                ['jpg', 'jpeg', 'png'],
                "Only jpg and jpeg along with png are allowed.",
            )
        ], null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @cached_property
    def thumbnail(self):
        html = '<img src="{img}" height="20px" width="20px" style="border-radius: 50%">'
        if self.image:
            return format_html(html, img=self.image.url)
        return (
            format_html('<strong>There is no image for this entry.<strong>'))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, self.created_at)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):
    slug = models.SlugField()
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to='image/subcategory/', validators=[
            FileExtensionValidator(
                ['jpg', 'jpeg', 'png'],
                "Only jpg and jpeg along with png are allowed.",

            )
        ]
    )
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    name = models.CharField(max_length=50, validators=[MinLengthValidator(3), ], unique=True)

    class Meta:
        db_table = 'Subcategories'
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, self.created_at)

        super().save(*args, **kwargs)
