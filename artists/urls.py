from django.urls import path
from . import views

urlpatterns = [
    path('dbsave/', views.dbsaveView),
    path('dbPkReset/',views.dbPkResetView)
]