from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', updatelist.as_view()),
    path('', readlist.as_view()),
    path('create', createlist.as_view()),
    path('delete/<int:pk>', deletelist.as_view()),
]
