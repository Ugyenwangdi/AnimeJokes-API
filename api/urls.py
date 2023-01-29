from django.urls import path  
from . import views 

from rest_framework_simplejwt.views import ( 
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [ 
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.getRoutes),
    path('jokes/', views.getJokes),
    path('jokes/<str:pk>/', views.getJoke),

    path('animes/', views.getAnimes),
    path('animes/<str:pk>/', views.getAnime),

]