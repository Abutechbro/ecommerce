
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('all_product/', views.all_product, name="prod"),
    path('logout/', views.logout_user, name="logout"),
    path('login/', views.login_user, name="login"),
    path('register/', views.register_user, name="register"),
    path('product_details/<int:pk>', views.product_details, name="product_details"),
    path('admin_dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('category/<str:foo>', views.category, name="category"),
]
