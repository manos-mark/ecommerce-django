from django.urls import path

from . import views

urlpatterns = [
    # Leave as empty string for base url
    path('', views.store, name="store"),
    path('category/', views.category, name="category"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('proccess_order/', views.proccessOrder, name="proccess_order"),
]
