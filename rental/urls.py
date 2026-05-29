from django.urls import path
from . import views

app_name = 'rental'

urlpatterns = [
    # Public pages
    path('', views.landing_page, name='landing'),
    path('katalog/', views.catalog, name='catalog'),
    path('alat/<int:pk>/', views.equipment_detail, name='equipment_detail'),
    path('booking/', views.booking_form, name='booking'),
    path('booking/success/', views.booking_success, name='booking_success'),
    
    # Admin auth
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    
    # Admin dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Admin equipment CRUD
    path('dashboard/alat/', views.equipment_list, name='equipment_list'),
    path('dashboard/alat/tambah/', views.equipment_create, name='equipment_create'),
    path('dashboard/alat/<int:pk>/edit/', views.equipment_edit, name='equipment_edit'),
    path('dashboard/alat/<int:pk>/hapus/', views.equipment_delete, name='equipment_delete'),
    
    # Admin booking management
    path('dashboard/booking/', views.booking_list, name='booking_list'),
    path('dashboard/booking/<int:pk>/status/', views.booking_update_status, name='booking_update_status'),
    path('dashboard/booking/<int:pk>/hapus/', views.booking_delete, name='booking_delete'),
]
