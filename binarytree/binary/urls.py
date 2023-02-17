from . import views
from django.urls import path

urlpatterns = [
    path('',views.binary_tree_view,name='binary_tree_view'),
]
