from django.urls import path, include
from . import views

urlpatterns = [
    path("hello/", views.hello_world, name="hello"),
    path("main/", views.main, name="main"),
    path("service/", views.service, name="service"),
    path("about/", views.about, name="about"),
    path("order/", views.order, name="order"),
    path("form/postuser/", views.form, name="postuser"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('form/', views.form, name="form"),
]
