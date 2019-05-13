from django.contrib import admin
from django.urls import path
import products.views

urlpatterns = [
	path('', products.views.home, name="products_home"),
	path('create/',products.views.create, name="products_create"),
	path('<int:product_id>/', products.views.detail, name="products_detail"),
	path('<int:product_id>/upvote/',products.views.upvote,name="products_upvote")
]