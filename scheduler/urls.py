from django.urls import path

from . import views

app_name = "scheduler"

urlpatterns = [
    path('', views.index, name='index'),
    path("makeorg", views.makeorg, name="makeorg"),
    path("makeuser",views.makeuser,name="makeuser"),
    path("join", views.joinorg, name="joinorg"),
]
