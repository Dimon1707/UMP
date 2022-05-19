from django.urls import path
from core.views import register, main, groups, news, profile

urlpatterns = [
    # 1-путь,2-функция,3-кр.название
    path('', main, name='main'),
    path('register/', register, name='register'),
    path('groups/', groups, name='groups'),
    path('news/', news, name='news'),
    path('profile/', profile, name='profile'),

]