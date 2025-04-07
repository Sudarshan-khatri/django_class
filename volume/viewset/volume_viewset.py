from rest_framework import viewsets
from ..models import Volume
from ..volume_serialize.serializer import*
from ..utilities.pagination import PageNumberPagination



class VolumeViewset(viewsets.ModelViewSet):
    serializer_class=VolumeListSerializer
    queryset=Volume.objects.all().order_by('-id')
    pagination_class=PageNumberPagination
    





    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset
    

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return VolumeRetrieveSerializer
        elif self.action =='retrieve':
            return VolumeWriteSerializer
        return super().get_serializer_class()
    
