from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from .views import Home, CategoryByProducts, ProductDetailView, Search

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', CategoryByProducts.as_view(), name='category'),
    path('products/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('search/', Search.as_view(), name='search')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)