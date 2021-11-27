from django.urls import path, include

from art.api.views import GetAllArtsAPI, GetARandomArtAPI, GetArtAPI

urlpatterns = [
    path('', GetAllArtsAPI.as_view()),
    path('<int:pk>/', GetArtAPI.as_view()),
    path('random/', GetARandomArtAPI.as_view()),
]