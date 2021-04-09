from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

router = routers.DefaultRouter()
router.register(r'lists',views.ListViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_view'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]