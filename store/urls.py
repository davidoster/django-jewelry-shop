from django.urls import path
from . import views


app_name = 'store'


urlpatterns = [
    path('', views.home, name="home"),
    path('product/<slug:slug>/', views.detail, name="product-detail"),
    path('categories/', views.all_categories, name="all-categories"),
    path('<slug:slug>/', views.category_products, name="category-products"),

    path('shop/', views.shop, name="shop"),

    # URL for Authentication
    path('accounts/register/', views.register, name="register"),
    path('accounts/register_save/', views.register_save, name="register_save"),
    path('accounts/login/', views.login, name="login"),

    path('product/test/', views.test, name="test"),

    path('product/add-to-cart/', views.add_to_cart, name="add-to-cart"),
    path('product/cart/', views.cart, name="cart"),
    path('product/checkout/', views.checkout, name="checkout"),
]
