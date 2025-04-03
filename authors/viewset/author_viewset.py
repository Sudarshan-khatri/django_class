from rest_framework import viewsets
from ..models import Author
from ..serializer.author_serializer import*



class AuthorViewset(viewsets.ModelViewSet):
    serializer_class=AuthorListSerializer
    queryset=Author.objects.all().order_by('-id')
    





    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset
    

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return AuthorsWriteSerializer
        elif self.action =='retrieve':
            return AuthorsRetrieveSerializer
        return super().get_serializer_class()
    
