from rest_framework.routers import DefaultRouter
from ..viewset.author_viewset import AuthorViewset


router=DefaultRouter()
router.register('author',AuthorViewset,basename='authors')