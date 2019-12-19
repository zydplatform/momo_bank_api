from django.urls import path
from authentication import views

app_name = "authentication"
urlpatterns = [
    path('signup/', views.UserView.as_view(), name='signup'),
]