from django.urls import path
from accounts import views

urlpatterns = [
    path('google_login/', views.google_login, name='google_login'),
    path('google_withdrawal/', views.google_withdrawal, name='google_withdrawal'),
    path('fav_char_update/', views.fav_char_update, name='fav_char_update'),
    path('fav_char/', views.fav_char, name='fav_char'),
]
