from django.conf.urls import url, include
from rest_framework import routers
# from django.conf import settings
# from User import views as user_views
from User import views

router = routers.SimpleRouter()
router.register(r'operation', views.CustomerProfileViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]