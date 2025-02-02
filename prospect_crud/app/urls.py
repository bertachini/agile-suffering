from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # Authentication URLs
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', LogoutView.as_view(
        template_name='logged_out.html',
        next_page='login',
        http_method_names=['get', 'post']
    ), name='logout'),
    
    # Main pages
    path('', views.home, name='home'),
    
    # Lead management URLs
    path('leads/', views.lead_list, name='lead_list'),
    path('leads/create/', views.lead_create, name='lead_create'),
    path('leads/<int:pk>/', views.lead_detail, name='lead_detail'),
    path('leads/<int:pk>/update/', views.lead_update, name='lead_update'),
    path('leads/<int:pk>/delete/', views.lead_delete, name='lead_delete'),
]
