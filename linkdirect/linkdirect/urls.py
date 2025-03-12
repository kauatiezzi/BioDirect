# linkdirect/urls.py
from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.conf.urls.static import static
from django.conf import settings

handler404 = 'myapp.views.error_404_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Página inicial
    path('login/', views.login_view, name='login'),  # Página de login
    path('logout/', views.logout_view, name='logout'),  # Página de logout
    path('accounts/', include('django.contrib.auth.urls')),  # Inclui URLs de autenticação padrão
    path('em-breve/', views.em_breve, name='em_breve'),
    path('<str:username>/', views.profile, name='profile'),
    path('edit_profile/<str:username>/', views.edit_profile, name='edit_profile'),
    path('delete-button/<int:button_id>/', views.delete_button, name='delete_button'),
    path('create-profile/', views.create_profile, name='create_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)