from django.urls import path
from tree_view import views


urlpatterns = [
    path("",
         views.generate_tree,
         name="generate_tree"),
]
