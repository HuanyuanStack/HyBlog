from django.urls import path

from . import views

app_name = "blog_app"
urlpatterns = [
    path('', views.index, name='index'),
    path('go_add_user/', views.go_add_user, name='go_add_user'),
    path('add_user/', views.add_user, name='add_user'),
]