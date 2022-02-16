from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (CategoryByProducts, Home, ProductDetailView, Search,
                    contacts, thanks)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', CategoryByProducts.as_view(), name='category'),
    path('products/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('search/', Search.as_view(), name='search'),
    path('contacts/', contacts, name='contacts'),
    path('thanks/', thanks, name='thanks'),

  ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
