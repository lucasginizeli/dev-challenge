from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('', views.index),
    path('list/<slug:tipo>', views.list, name='list'),
    path('edit/<slug:tipo>/<int:pk>', views.edit, name='edit'),
    path('delete/<slug:tipo>/<int:pk>', views.delete, name='delete'),
    path('upload_csv/', views.upload_csv, name='upload_csv'),
]
