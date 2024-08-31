from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),                                # returns or redirects to webpage
     path('studio_register', views.createStudioProfile),  # returns JSON -- handle response->action in HTML   
    path('user_register', views.createUserProfile),      # returns JSON -- handle response->action in HTML
]