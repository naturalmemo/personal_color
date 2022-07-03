from django.urls import path
from . import views

app_name = 'personal_color'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
