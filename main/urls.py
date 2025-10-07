# main/urls.py

from django.urls import path
from main.views import (
    show_main, register, login_user, logout_user,
    get_products_json, add_product_ajax, delete_product_ajax,
    get_product_detail_json, edit_product_ajax,
    register_ajax, login_ajax, get_product_for_detail_view_json
)

app_name = 'main'

urlpatterns = [
    # Page rendering
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    # Product AJAX API
    path('get-products/', get_products_json, name='get_products_json'),
    path('add-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('delete-product-ajax/<uuid:id>/', delete_product_ajax, name='delete_product_ajax'),
    path('get-product-detail-json/<uuid:id>/', get_product_detail_json, name='get_product_detail_json'),
    path('edit-product-ajax/<uuid:id>/', edit_product_ajax, name='edit_product_ajax'),
    path('get-product-for-detail-view-json/<uuid:id>/', get_product_for_detail_view_json, name='get_product_for_detail_view_json'),

    # Auth AJAX API
    path('register-ajax/', register_ajax, name='register_ajax'),
    path('login-ajax/', login_ajax, name='login_ajax'),
]