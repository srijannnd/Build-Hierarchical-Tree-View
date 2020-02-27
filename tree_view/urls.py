from django.urls import path
from tree_view import views


urlpatterns = [
    path("",
         views.generate_tree,
         name="generate_tree"),
    path("<str:company>/",
         views.generate_tree_view,
         name="generate_tree_view")
]
