from django.urls import path
from accounts import views

urlpatterns = [
     path('google_login/', views.google_login, name='google_login'),
     path('fav_char_update/', views.fav_char_update, name='fav_char_update'),
]
