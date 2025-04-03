"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from .import views
from rest_framework import routers
from book.routers.routers  import router as book_router
from authors.routers.routers import router as author_router
from publication.routers.routers import router as publication_router
from reviews.router.router  import router as review_router
from volume.router.router import router as volume_router


#set the default register
router=routers.DefaultRouter()

router.registry.extend(book_router.registry)
router.registry.extend(author_router.registry)
router.registry.extend(publication_router.registry)
router.registry.extend(review_router.registry)
router.registry.extend(volume_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('api/',include(router.urls))
]

