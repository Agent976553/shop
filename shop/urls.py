from django.urls import path
from.import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('orders/', views.orders, name='orders'),
    path('ordercreate/', views.order_create, name='order_create'),
]