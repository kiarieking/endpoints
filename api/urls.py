from django.urls import path, include

from api import views
from .views import *

urlpatterns = [
    path("products/", product_list_view),
    path("categories/", all_categories),
    path('category/products/<category_name>', views.get_filtered_products),
    path('cart/<int:buyer_id>', views.cart),
    path('add_to_cart', views.add_to_cart, name="image"),
    path('add_to_wishlist', views.add_to_wishlist),
    path('wishlist/<int:buyer_id>', views.wishlist),
    path('remove_from_cart/<int:product_id>', views.remove_from_cart),
    path('login', login),
    path('register', register)
    ]
