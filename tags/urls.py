from django.urls import path
from tags.views import *

app_name = 'tag'

urlpatterns = [
    path('', TagListView.as_view(), name='list'),
    path('create/', TagCreateView.as_view(), name='create'),
    path('update/<slug:slug>', TagUpdateView.as_view(), name='update'),
    path('remove/<slug:slug>', TagRemoveView.as_view(), name='remove'),
]
