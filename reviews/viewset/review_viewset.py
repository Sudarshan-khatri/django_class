from rest_framework import viewsets
from ..models import Reviews
from ..review_serializer.serializer import*
from ..utilities.pagination import PageNumberPagination



class ReviewsViewset(viewsets.ModelViewSet):
    serializer_class=ReviewsListSerializer
    queryset=Reviews.objects.all().order_by('-id')
    pagination_class=PageNumberPagination
    





    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset
    

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return ReviewsRetrieveSerializer
        elif self.action =='retrieve':
            return ReviewsWriteSerializer
        return super().get_serializer_class()
    
