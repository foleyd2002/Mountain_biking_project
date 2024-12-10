from django.urls import path
from . import views

urlpatterns = [
    path('', views.trail_list, name='home'),
    path('trail/<int:trail_id>/', views.trail_detail, name='trail_detail'),
    path('about/', views.about_page, name='about'), 
    path('contact/', views.contact_page, name='contact'),
    path('athlete/', views.athlete_detail, name='athlete_page'),
    path('admin/', views.admin_page, name='admin_page'),
    path('<int:num1>/<int:num2>/<int:num3>/',views.magic, name='magic'),
    path('magic1/', views.magic1, name='magic1'), 
]
