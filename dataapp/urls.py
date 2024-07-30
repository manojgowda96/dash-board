from django.urls import path
from .views import DataList
from . import views

urlpatterns = [
    path('data/', DataList.as_view(), name='data-list'),
    path('index/',views.index,name='index'),
]