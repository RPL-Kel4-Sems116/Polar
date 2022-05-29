from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home2, name='home'),
    path('order/', views.order, name='order'),
    path('list/', views.list, name='list'),
    path('register/', views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('gambar/<int:gambar_id>', views.gambar)
]

