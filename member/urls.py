from django.urls import path
from.import views

urlpatterns = [
    path('lg_su/',views.log_vw),
    path('login/',views.login_user),
    path('home/',views.home)
    
]