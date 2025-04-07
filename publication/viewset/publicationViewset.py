from rest_framework import viewsets
from ..models import Publication
from ..publication_serializer.serializer import*
from ..utilities.pagination import PageNumberPagination


class PublicationViewset(viewsets.ModelViewSet):
    serializer_class=PublicationListSerializer
    queryset=Publication.objects.all().order_by('-id')
    pagination_class=PageNumberPagination
    





    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset
    

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return PublicationRetrieveSerializer
        elif self.action =='retrieve':
            return PublicationWriteSerializer
        return super().get_serializer_class()
    
