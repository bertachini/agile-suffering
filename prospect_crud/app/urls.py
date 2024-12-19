from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # URLs de autenticação
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    # Página inicial
    path('', views.home, name='home'),  # Rota para 'home'

    # URLs existentes
    path('leads/', views.lead_list, name='lead_list'),
    path('leads/create/', views.lead_create, name='lead_create'),
    path('leads/<int:pk>/update/', views.lead_update, name='lead_update'),
    path('leads/<int:pk>/delete/', views.lead_delete, name='lead_delete'),
    path('leads/<int:pk>/', views.lead_detail, name='lead_detail'),
]
