from rest_framework.routers import DefaultRouter
from ..viewsets.Book_viewset import bookViewer


router=DefaultRouter()

router.register('book',bookViewer,basename='book')