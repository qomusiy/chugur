from django.urls import path
from .views import singup, user_login, user_logout, user_update, user_delete
urlpatterns = [
    path('singup/', singup, name='singup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('update/', user_update, name='update'),
    path('delete/', user_delete, name='delete'),

]