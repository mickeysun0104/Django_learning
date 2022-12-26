"""d_learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from music import views as mv
from rest_framework.routers import DefaultRouter
from django.conf.urls import include


router = DefaultRouter()
router.register(r'music', mv.MusicViewSet)
print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('hi/<username>/', views.hiname),
    path('age/<int:year>/', views.age),
    path('hello/', views.hello_view),
    path('getName/<username>/', views.getOneByName), # 傳遞字串參數 username
    path('getAll/', views.getAll),
    path('login/', views.login),
    path('music/', mv.music_view),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
