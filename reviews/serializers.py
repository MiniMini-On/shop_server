from rest_framework import serializers
from .models import Review
from users.serializers import UserNameSerializer
from order_details.serializers import ReviewOrderDetailSerializer

class ProductReviewSerializer(serializers.ModelSerializer):
    user = UserNameSerializer(read_only = True)
    order_detail = ReviewOrderDetailSerializer(read_only = True)
    class Meta:
        model = Review
        fields = ('user', 'order_detail', 'content', 'rating', 'best')