from django.urls import include, path
from rest_framework import routers
#from .views import UserViewSet
from .views import ( UserListApiView, UserDetailApiView)
router = routers.DefaultRouter()
#router.register(r'users',UserViewSet)

urlpatterns = [
    #path('',include(router.urls))
    path('users/', UserListApiView.as_view()),
    path('users/<int:user_id>/', UserDetailApiView.as_view())
]