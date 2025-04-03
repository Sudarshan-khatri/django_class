from  rest_framework.routers import DefaultRouter
from ..viewset.volume_viewset import VolumeViewset

router=DefaultRouter()
router.register('volume',VolumeViewset,basename='volume')