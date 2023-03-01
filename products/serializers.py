from rest_framework import serializers
from .models import Product
from artists.serializers import ProductArtistSerializer
from product_categories.serializers import ProductCategorySerializer
from product_options.serializers import ProductOptionSerializer
from themes.serializers import ProductThemeSerializer
from reviews.serializers import ProductReviewSerializer

class ProductsSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(read_only = True)
    theme = ProductThemeSerializer(read_only = True)
    artist = ProductArtistSerializer(read_only = True)
    
    class Meta:
        model = Product
        fields = ('id','name','category','theme', 'artist','image1','price','hits','like')
        
class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(read_only = True)
    artist = ProductArtistSerializer(read_only = True)
    option= ProductOptionSerializer(read_only = True)
    review_set = ProductReviewSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = ('id','name','category','artist','option','image1','image2','price','stock','like','review_set')
        
class OrderDetailProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name',)