from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("users.urls")),
    path("api/artists/", include("artists.urls")),
    path("api/products/", include("products.urls")),
    path("api/carts/", include("carts.urls")),
    path("api/orders/", include("orders.urls")),
    
]
