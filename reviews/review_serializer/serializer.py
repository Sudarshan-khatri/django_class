from rest_framework  import serializers
from ..models import Reviews


class ReviewsListSerializer(serializers.ModelSerializer):
    class meta:
        model=Reviews
        fields=['name','rating','book_name','description','created_date','updated_date']





#class to retrieve from the models:
class ReviewsRetrieveSerializer(serializers.ModelSerializer):
    class meta:
        model=Reviews
        fields=['name','rating','book_name']

#class to write from the models
class ReviewsWriteSerializer(serializers.ModelSerializer):
    class meta:
        model=Reviews
        fields="__all__"