from  rest_framework.routers import DefaultRouter
from ..viewset.publicationViewset import PublicationViewset

router=DefaultRouter()
router.register('publication',PublicationViewset,basename='publication')
