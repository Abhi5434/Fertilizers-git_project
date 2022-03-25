from django.urls import path
from .import views
urlpatterns = [
   path('', views.Register),
    path('', views.Login),

]