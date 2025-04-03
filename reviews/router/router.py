from  rest_framework.routers import DefaultRouter
from ..viewset.review_viewset import ReviewsViewset

router=DefaultRouter()
router.register('review',ReviewsViewset,basename='review')