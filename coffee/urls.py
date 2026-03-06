from django.contrib import admin
from django.urls import path
from coffee import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    path('add-to-cart/<int:coffee_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/<int:item_id>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('remove-cart-item/<int:item_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('about/', views.About, name='about'),
    path('mycart/', views.My_Cart, name='mycart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.Contact, name='contact'),
    path("order-success/", views.order_success, name="order_success"),
    

]






