from django.urls import path,include
from rest_framework import routers
from cars import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'cars', views.CarViewSet)
router.register(r'ads', views.AdsViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'marks', views.MarkViewSet)
router.register(r'models', views.MadelViewSet)
router.register(r'colors', views.ColorViewSet)


urlpatterns= [
    path('',include(router.urls))
]