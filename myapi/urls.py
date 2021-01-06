from django.urls import include,path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'waifu',views.waifuViewSet,basename="queryset")
router.register(r'image',views.imageViewSet,basename="queryset")
urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',
                             namespace= 'rest_framework'),)
]