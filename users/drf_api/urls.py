from django.urls import include, path
from rest_framework import routers
#from .views import UserViewSet
from .views import UserListApiView
router = routers.DefaultRouter()
#router.register(r'users',UserViewSet)

urlpatterns = [
    #path('',include(router.urls))
    path('', UserListApiView.as_view())
]