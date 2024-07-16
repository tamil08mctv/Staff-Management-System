from django.urls import path
from . import views 

urlpatterns = [
    path('register/',views.register,name="register_user"),
    path('login/',views.login,name="login_user"),
    path('logout/',views.logout,name="logout_user"),
]
