from django.urls import path,include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name = 'hello-viewset')
router.register('profiles', views.UserProfileViewset)
router.register('feed', views.ProfileFeedViewSet)

urlpatterns = [
path('hello-view/', views.HelloApiView.as_view()),
path('login/', views.UserloginAPIView.as_view()),
path('',include(router.urls))
]
