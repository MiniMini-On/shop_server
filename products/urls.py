from django.urls import path
from . import views

urlpatterns = [
    # path('dbsave/', views.dbsaveView),
    # path('dbPkReset/',views.dbPkResetView),
    path('',views.ProductsView.as_view()),
    path('<int:product_id>',views.ProductView.as_view()),
    
]